from application import app, db
from flask import Flask, request, jsonify, make_response

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Reddy42 Back End",
        "endpoints": [
            "GET / -fetches this messege" ,
            "Get /history/id -fetches patient medical history"
        ]
    }), 200
