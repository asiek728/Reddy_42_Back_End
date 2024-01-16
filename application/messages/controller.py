from flask import jsonify, request
from werkzeug import exceptions
from .model import Message
from .. import db

def get_messages_by_room_id(room_id):
    try:
        messages = Message.query.filter_by(room=room_id).all()

        if messages:
            message_data = [message.json() for message in messages]
            return jsonify({ "data": message_data }), 200
        else:
            return jsonify({ "data": [] }), 200

    except Exception as e:
        print(e)
        raise exceptions.InternalServerError("Error retrieving messages!")
