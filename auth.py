from flask import Blueprint, jsonify, request
from application.patients.model import Patient

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.post("/register")
# def register_user():

#     data = request.get_json()

#     user = Patient.get_user_by_email(email=data.get("email"))

#     if user is not None:
#         return jsonify({"error": "User already exists"}), 409

#     new_patient = Patient(first_name=data.get("first_name"), last_name=data.get("last_name"), email=data.get("email"), password=data.get("password"), nhs_number=data.get("nhs_number"), date_of_birth=data.get("date_of_birth"), sex=data.get("sex"), ethnicity=data.get("ethnicity"))

#     new_patient.set_password(password=data.get("password"))

#     new_patient.save()

#     return jsonify({"message": "User created"}), 201

## this is giving me errors for some reason - will need to check with romeo




