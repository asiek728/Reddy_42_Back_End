from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controller import get_conditions, get_condition_by_id, create_condition, update_condition, destroy_condition, get_user_conditions

@app.route('/conditions', methods=["GET", "POST"])
def handle_conditions():
    if request.method == "POST": return create_condition()
    if request.method == "GET": return get_conditions()


@app.route('/conditions/users/<int:patient_id>', methods=["GET"])
def handle_user_conditions(patient_id):
    if request.method == "GET": return get_user_conditions(patient_id)


@app.route('/conditions/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_condition(id):
    if request.method == "GET": return get_condition_by_id(id)
    if request.method == "PATCH": return update_condition(id)
    if request.method == "DELETE": return destroy_condition(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
