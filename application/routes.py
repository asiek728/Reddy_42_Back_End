from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Reddy42 Back End",
        "endpoints": [
            "GET /"
        ]
    }), 200
