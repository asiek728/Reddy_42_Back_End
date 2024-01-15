from flask_socketio import emit, join_room
from application import socketio, db
from application.models import Message
from flask_cors import CORS
from flask import request

CORS(socketio)

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
    room = data['room']
    message_content = data['content']
    author = data['author']
    time = data['time']

    new_message = Message(content=message_content, author=author, room=room, time=time)
    db.session.add(new_message)
    db.session.commit()

    emit('receive_message', data, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    print(f'User Disconnected: {request.sid}')