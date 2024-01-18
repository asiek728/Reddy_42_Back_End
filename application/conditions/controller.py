from flask import jsonify, request
from werkzeug import exceptions
from .model import Condition
from .. import db
import base64

# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     jwt_required,
#     get_jwt,
#     current_user,
#     get_jwt_identity,
# )

from flask_jwt_extended import jwt_required, get_jwt
from application.patients.model import Patient, TokenBlocklist
from schemas import UserSchema


def get_conditions():
    # claims = get_jwt()

    # if claims.get("is_staff") == True:
        condition = Condition.query.all()
        try:
            return jsonify({ "data": [c.json for c in condition] }), 200
        except:
            raise exceptions.InternalServerError(f"Conditions not found!")
        
    # return jsonify({"message": "You are not authorized to access this"}), 401
    

def get_user_conditions(patient_email):

    print("patient_id", type(id))
    conditions = Condition.query.filter_by(patient_email=patient_email).all()
    try:
        return jsonify({ "data": [c.json for c in conditions] }), 200
    except:
        raise exceptions.InternalServerError(f"User history not found!")


def get_condition_by_id(id):
    print("id", type(id))
    condition = Condition.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": condition.json }), 200
    except:
        raise exceptions.NotFound(f"Condition not found!")


def create_condition():
    try:
        patient_email, condition_name, description, start_date, end_date, image = request.json.values()

        binary_image = base64.b64decode(image)

        new_condition = Condition(patient_email, condition_name, description, start_date, end_date, binary_image)

        db.session.add(new_condition)
        db.session.commit()

        return jsonify({ "data": new_condition.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update_condition(id):
    claims = get_jwt()

    if claims.get("is_staff") == True:
        data = request.json
        condition = Condition.query.filter_by(id=id).first()

        for (attribute, value) in data.items():
            if hasattr(condition, attribute):
                setattr(condition, attribute, value)

        db.session.commit()
        return jsonify({ "data": condition.json })
    
    return jsonify({"message": "You are not authorized to access this"}), 401


def destroy_condition(id): 
    claims = get_jwt()

    if claims.get("is_staff") == True:

        condition = Condition.query.filter_by(id=id).first()
        db.session.delete(condition)
        db.session.commit()
        return "Condition Deleted", 204

    return jsonify({"message": "You are not authorized to access this"}), 401
