from flask_socketio import emit, join_room
from flask_socketio import SocketIO
from application import db
from application.messages.models import Message
from flask_cors import CORS
from flask import request

# socketio = SocketIO()

# CORS(socketio)


def init_socketio_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print(f'User Connected: {request.sid}')

    @socketio.on('join_room')
    def handle_join_room(data):
        room = data['room']
        join_room(room)
        print(f'User with ID: {request.sid} joined room: {room}')

    @socketio.on('send_message')
    def handle_send_message(data):
        print(f"Received message: {data}")
        room = data['room']
        message_content = data['content']
        author = data['author']
        time = data['time']

        emit('receive_message', data, room=room)

    @socketio.on('disconnect')
    def handle_disconnect():
        print(f'User Disconnected: {request.sid}')