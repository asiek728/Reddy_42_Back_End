from flask import jsonify, request
from werkzeug import exceptions
from .model import HereditaryCondition
from .. import db

from application.patients.model import Patient, TokenBlocklist
from schemas import UserSchema


def get_conditions():
    # claims = get_jwt()

    # if claims.get("is_staff") == True:
        condition = HereditaryCondition.query.all()
        try:
            return jsonify({ "data": [c.json for c in condition] }), 200
        except:
            raise exceptions.InternalServerError(f"Hereditary conditions not found!")
    

def get_user_conditions(email):
    print("patient_id", type(id))
    conditions = HereditaryCondition.query.filter_by(email=email).all()
    try:
        return jsonify({ "data": [c.json for c in conditions] }), 200
    except:
        raise exceptions.InternalServerError(f"User history not found!")


# def get_condition_by_id(id):
#     print("id", type(id))
#     condition = HereditaryCondition.query.filter_by(id=id).first()
#     try:
#         return jsonify({ "data": condition.json }), 200
#     except:
#         raise exceptions.NotFound(f"Hereditary Condition not found!")


def create_condition():
    try:
        email, hereditary_condition_name = request.json.values()

        new_condition = HereditaryCondition(email, hereditary_condition_name)

        db.session.add(new_condition)
        db.session.commit()

        return jsonify({ "data": new_condition.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

# def update_condition(id):
#     data = request.json
#     condition = HereditaryCondition.query.filter_by(id=id).first()

#     for (attribute, value) in data.items():
#         if hasattr(condition, attribute):
#             setattr(condition, attribute, value)

#     db.session.commit()
#     return jsonify({ "data": condition.json })

# def destroy_condition(id):
#     condition = HereditaryCondition.query.filter_by(id=id).first()
#     db.session.delete(condition)
#     db.session.commit()
#     return "Hereditary Condition Deleted", 204
