from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controller import get_conditions,  create_condition, get_user_conditions   #, get_condition_by_id, update_condition, destroy_condition

from flask_jwt_extended import jwt_required, get_jwt

@app.route('/hereditary_conditions', methods=["GET", "POST"])
# @jwt_required()
def handle_hereditary_conditions():
    if request.method == "POST": return create_condition()
    if request.method == "GET": return get_conditions()


@app.route('/hereditary_conditions/users/<email>', methods=["GET"])
# @jwt_required()
def handle_user_hereditary_conditions(email):
    if request.method == "GET": return get_user_conditions(email)


# @app.route('/hereditary_conditions/<int:id>', methods=["GET", "PATCH", "DELETE"])
# # @jwt_required()
# def handle_hereditary_condition(id):
#     if request.method == "GET": return get_condition_by_id(id)
#     if request.method == "PATCH": return update_condition(id)
#     if request.method == "DELETE": return destroy_condition(id)
