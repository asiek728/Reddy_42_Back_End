from flask import jsonify, request
from werkzeug import exceptions
from .model import Condition
from .. import db

def get_conditions():
    condition = Condition.query.all()
    try:
        return jsonify({ "data": [c.json for c in condition] }), 200
    except:
        raise exceptions.InternalServerError(f"Conditions not found!")

def get_condition_by_id(id):
    print("id", type(id))
    condition = Condition.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": condition.json }), 200
    except:
        raise exceptions.NotFound(f"Condition not found!")


def create_condition():
    try:
        condition_id, condition_name, description, start_date, end_date = request.json.values()

        new_condition = Condition(condition_id, condition_name, description, start_date, end_date)

        db.session.add(new_condition)
        db.session.commit()

        return jsonify({ "data": new_condition.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update_condition(id):
    data = request.json
    condition = Condition.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(condition, attribute):
            setattr(condition, attribute, value)

    db.session.commit()
    return jsonify({ "data": condition.json })

def destroy_condition(id):
    condition = Condition.query.filter_by(id=id).first()
    db.session.delete(condition)
    db.session.commit()
    return "Patient Deleted", 204
