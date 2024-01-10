from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controller import get_patient_info, create_patient, update_patient, destroy_patient


@app.route('/patient', methods=["POST"])
def handle_patients():
    if request.method == "POST": return create_patient()

@app.route('/patient/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_patient(id):
    if request.method == "GET": return get_patient_info(id)
    if request.method == "PATCH": return update_patient(id)
    if request.method == "DELETE": return destroy_patient(id)
 

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
