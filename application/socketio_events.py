from flask_socketio import emit, join_room
from flask_socketio import SocketIO
from application import db
from application.messages.model import Message
from flask_cors import CORS
from flask import request



def init_socketio_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print(f'User Connected: {request.sid}')

    @socketio.on('join_room')
    def handle_join_room(data):
        room = data['room']
        join_room(room)
        print(f'User with ID: {request.sid} joined room: {room}')

    @socketio.on('user_joined')
    def handle_user_joined(data):
        room = data['room']
        username = data['username']
        print(data)
        emit('receive_message', {'content': f'{username} joined the room', 'author': 'System', 'time': 'now'}, room=room)

    @socketio.on('send_message')
    def handle_send_message(data):
        print(f"Received message: {data}")
        room = data['room']
        message_content = data['content']
        author = data['author']
        time = data['time']

        new_message = Message(room=room, author=author, content=message_content, time=time)

        try:
            db.session.add(new_message)
            
            db.session.commit()

            emit('receive_message', data, room=room)

        except Exception as e:
            print(f"Error saving message: {e}")

    

    # @socketio.on('user_left')
    # def handle_user_left(data):
    #     room = data['room']
    #     username = data['username']
    #     emit('receive_message', {'content': f'{username} left the room.', 'author': 'System', 'time': 'now'}, room=room)
        
    @socketio.on('disconnect')
    def handle_disconnect():
        print(f'User Disconnected: {request.sid}')