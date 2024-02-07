from flask import Blueprint, jsonify, request
from werkzeug import exceptions
from .model import Patient

#########################################
# auth_bp = Blueprint("auth", __name__)

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    current_user,
    get_jwt_identity,
)

from flask_jwt_extended import jwt_required, get_jwt
from application.patients.model import Patient, TokenBlocklist
from schemas import UserSchema
#########################################

from .. import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

def get_patients():
    patient = Patient.query.all()
    try:
        return jsonify({ "data": [c.json for c in patient] }), 200
    except:
        raise exceptions.InternalServerError(f"Patient not found!")
    

def get_patient_info(patient_email):
    # print("id", type(id))
    patient = Patient.query.filter_by(email=patient_email).first()
    try:
        return jsonify({ "data": patient.json }), 200
    except:
        raise exceptions.NotFound(f"Patient not found!")
    
def get_user_family(patient_email):
    patient = Patient.query.filter_by(email=patient_email).first()

    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    
    family_members = patient.related_to

    family_data = []
    for member in family_members:
        hereditary_conditions = []
        for condition in member.hereditary_conditions:
            hereditary_conditions.append({"id": condition.id,"hereditary_condition_name": condition.hereditary_condition_name})
        family_data.append({
            'first_name': member.first_name,
            'last_name': member.last_name,
            'email': member.email,
            "hereditary_conditions": hereditary_conditions or ""
        })

    try:
        return jsonify({'family_members': family_data}), 200
    except:
        raise exceptions.InternalServerError(f"User history not found!")
    

def create_relationship():
    data = request.json

    # Check if required fields are present in the request
    if 'patient_email' not in data or 'related_patient_email' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    patient_email = data['patient_email']
    related_patient_email = data['related_patient_email']

    # Check if the patient emails exist in the database
    patient = Patient.query.filter_by(email=patient_email).first()
    related_patient = Patient.query.filter_by(email=related_patient_email).first()

    if not patient or not related_patient:
        return jsonify({'error': 'Patient not found'}), 404

    # Create the relationship
    patient.related_to.append(related_patient)
    db.session.commit()

    return jsonify({'message': 'Relationship created successfully'}), 201



###################################
# @auth_bp.post("/register")
###################################
def create_patient():
    try:
    ######################################################
        data = request.get_json()

        user = Patient.get_user_by_email(email=data.get("email"))

        if user is not None:
            return jsonify({"error": "User already exists"}), 409

        new_patient = Patient(first_name=data.get("first_name"), last_name=data.get("last_name"), email=data.get("email"), password=data.get("password"), nhs_number=data.get("nhs_number"), date_of_birth=data.get("date_of_birth"), sex=data.get("sex"), ethnicity=data.get("ethnicity"))

        print(new_patient)

        new_patient.set_password(password=data.get("password"))

        db.session.add(new_patient)
        db.session.commit()
    ######################################################

        return jsonify({ "data": new_patient.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request, sorry :(")


def update_patient(id):
    data = request.json
    patient = Patient.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(patient, attribute):
            setattr(patient, attribute, value)

    db.session.commit()
    return jsonify({ "data": patient.json })


def destroy_patient(id):
    patient = Patient.query.filter_by(id=id).first()
    db.session.delete(patient)
    db.session.commit()
    return "Patient Deleted", 204

#################################################################
def login_user():
    data = request.get_json()

    user = Patient.get_user_by_email(email=data.get("email"))

    if user and (user.check_password(password=data.get("password"))):
        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)
        user_email = data.get("email")

        return (
            jsonify(
                {
                    "message": "Logged In ",
                    "tokens": {"access": access_token, "refresh": refresh_token},
                    "user_id": user_email
                }
            ),
            200,
        )

    return jsonify({"error": "Invalid username or password"}), 400


def get_all_users():
    claims = get_jwt()

    if claims.get("is_staff") == True:
        page = request.args.get("page", default=1, type=int)

        per_page = request.args.get("per_page", default=3, type=int)

        users = Patient.query.paginate(page=page, per_page=per_page)

        result = UserSchema().dump(users, many=True)

        return (
            jsonify(
                {
                    "users": result,
                }
            ),
            200,
        )

    return jsonify({"message": "You are not authorized to access this"}), 401

def whoami():
    claims = get_jwt()
    return jsonify(
        {
            "message": "testing", 
            "claims":claims, #can remove this 
            "user_details": {
                "first_name": current_user.first_name,
                "email": current_user.email,
            }
        }
    )

## regain access route from refresh token 
def refresh_access():
    identity = get_jwt_identity()

    new_access_token = create_access_token(identity=identity)

    return jsonify({"access_token": new_access_token})

def logout_user():
    jwt = get_jwt()

    jti = jwt['jti']
    token_type = jwt['type']

    token_b = TokenBlocklist(jti=jti)

    token_b.save()

    return jsonify({"message": f"{token_type} token revoked successfully"}) , 200
#################################################################
