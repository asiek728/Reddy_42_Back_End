from application.messages.model import Message

def test_create_message():
    message1 = Message("room1", "author", "content", "time")

    assert message1.room == 'room1'
    assert message1.author == 'author'
    assert message1.content == 'content'
    assert message1.time == 'time'
    assert message1.__repr__() == f"Message('{message1.room}', '{message1.author}', '{message1.content}', '{message1.time}')"

    message1_json = message1.json()
    expected_json = {
        'id': message1.id,
        'room': 'room1',
        'author': 'author',
        'content': 'content',
        'time': 'time'
    }
    assert message1_json == expected_json
