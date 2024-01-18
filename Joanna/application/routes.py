from application import db
from flask import request, jsonify, Blueprint
from application.models import FriendsCharacter

characters = Blueprint("characters", __name__)

def format_character(character):
    return {
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@characters.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# POST 
@characters.route("/characters", methods=["POST"])
def create_character():
    # Retrieved data from client
    data = request.json
    # Created a new character using the data
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    # Send character to datbase
    db.session.add(character)
    db.session.commit()
    # Return JSON response back to the user/client
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@characters.route("/characters", methods=['GET'])
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return character_list

# GET /:id
@characters.route('/characters/<id>')
def get_character(id):
    # filter_by
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# DELETE /:id
@characters.route("/characters/<id>", methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character deleted {id}"

# PATCH /:id
@characters.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
    # Commit the change to the database
    db.session.commit()
    # Retrieve specific character from the filtering
    updatedCharacter = character.first()
    # Return JSON response to client 
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)
