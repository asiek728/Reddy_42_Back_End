from flask_socketio import emit
from application import db, socketio
from application.models import Message
from flask_cors import CORS
from flask import request


CORS(socketio)


@socketio.on('connect')
def handle_connect():
    socket_id = request.sid
    print(f"patiant {socket_id} connected")



@socketio.on('send_message')
def handle_message(data):
    message = Message(room=data['room'], author=data['author'], content=data['content'], time=data['time'])
    db.session.add(message)
    db.session.commit()
    emit('receive_message', {'room': data['room'], 'author': data['author'], 'content': data['content'], 'time': data['time']}, broadcast=True)