from application import db, app

app.app_context().push()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    time = db.Column(db.String(20), nullable=False)

    def __init__(self, room, author, content, time):
        self.room = room
        self.author = author
        self.content = content
        self.time = time

    def __repr__(self):
        return f"Message('{self.room}', '{self.author}', '{self.content}', '{self.time}')"
    
    def json(self):
        return {
            'id': self.id,
            'room': self.room,
            'author': self.author,
            'content': self.content,
            'time': self.time
        }