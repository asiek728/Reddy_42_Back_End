from flask import jsonify, request
from werkzeug import exceptions
from .model import Patient
from .. import db

def get_patient_info(id):
    print("id", type(id))
    patient = Patient.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": patient.json }), 200
    except:
        raise exceptions.NotFound(f"Patient not found!")


def create_patient():
    try:
        first_name, last_name, email, password, nhs_number, date_of_birth, sex, ethnicity  = request.json.values()

        new_patient = Patient(first_name, last_name, email, password, nhs_number, date_of_birth, sex, ethnicity)

        db.session.add(new_patient)
        db.session.commit()

        return jsonify({ "data": new_patient.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

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
