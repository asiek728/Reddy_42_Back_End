from flask import request, jsonify, Blueprint
from werkzeug import exceptions
from application import app
from .controller import get_messages_by_room_id

messages = Blueprint("messages", __name__)

@app.route('/messages/<string:room_id>', methods=["GET"])
def handle_messages(room_id):
    if request.method == "GET":
        return get_messages_by_room_id(room_id)
