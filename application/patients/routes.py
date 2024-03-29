from flask import request, jsonify, Blueprint
from werkzeug import exceptions
from application import app # app from __init__.
from .model import Patient
from .controller import get_patient_info, create_patient,  get_patients, login_user, get_all_users, whoami, refresh_access, logout_user, get_user_family, create_relationship

from flask_jwt_extended import jwt_required, get_jwt

patients = Blueprint("patients", __name__)


@app.route('/patients', methods=["GET", "POST"])
def handle_patients():
    if request.method == "POST": return create_patient()
    if request.method == "GET": return get_patients()  #/all is ne version  
    
@app.route("/patients/email/<string:email>", methods=["GET"])
def patient_by_email(email):
    patient = Patient.get_user_by_email(email)
    try:
        return jsonify({ "data": patient.json }),200
    except:
        raise exceptions.NotFound(f"Patient not found!")

@app.route('/patients/<patient_email>', methods=["GET", "PATCH", "DELETE"])
#@jwt_required()
def handle_patient(patient_email):
    if request.method == "GET": return get_patient_info(patient_email)
    # if request.method == "PATCH": return update_patient(patient_email)
    # if request.method == "DELETE": return destroy_patient(patient_email)

@app.route('/patients/<patient_email>/family', methods=["GET"])
# @jwt_required()
def handle_patient_family(patient_email):
    if request.method == "GET": return get_user_family(patient_email)

@app.route('/create_relationship', methods=['POST'])
def handle_adding_family():
    if request.method == "POST": return create_relationship()


###############################################################

@app.route('/login', methods=["POST"])
def handle_user():
   if request.method ==  "POST": return login_user()

@app.route('/all', methods=["GET"])
@jwt_required()
def handle_users():
   if request.method ==  "GET": return get_all_users()

@app.route("/whoami", methods=["GET"])
@jwt_required()
def user_info():
   if request.method ==  "GET": return whoami()

@app.route("/refresh", methods=["GET"])
@jwt_required(refresh=True)
def refresh_user_token():
   if request.method ==  "GET": return refresh_access()

@app.route("/logout", methods=["GET"])
@jwt_required(verify_type=False)
def logout_user_token():
   if request.method ==  "GET": return logout_user()
###############################################################
   

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
