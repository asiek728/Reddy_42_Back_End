from flask import request, jsonify, Blueprint
from werkzeug import exceptions
from application import app # app from __init__.
from .controller import get_conditions, get_condition_by_id, create_condition,get_user_conditions  #,  update_condition, destroy_condition, 

from flask_jwt_extended import jwt_required, get_jwt

conditions = Blueprint("conditions", __name__)

@app.route('/conditions', methods=["GET", "POST"])
# @jwt_required()
def handle_conditions():
    if request.method == "POST": return create_condition()
    if request.method == "GET": return get_conditions()


@app.route('/conditions/users/<patient_email>', methods=["GET"])
# @jwt_required()
def handle_user_conditions(patient_email):
    if request.method == "GET": return get_user_conditions(patient_email)


@app.route('/conditions/<int:id>', methods=["GET", "PATCH", "DELETE"])
# @jwt_required()
def handle_condition(id):
    if request.method == "GET": return get_condition_by_id(id)
    # if request.method == "PATCH": return update_condition(id)
    # if request.method == "DELETE": return destroy_condition(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
