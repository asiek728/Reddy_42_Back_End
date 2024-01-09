from application import app
from flask import request, jsonify, render_template, redirect
from application.models import Patient

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

@app.route("/patient/<id>")
def patient_info(id):
    return "<p>Returns into on a patient with id: {{id}}</p>"

@app.route("/history/<id>")
def patient_history(id):
    return "<p>Takes the id of a patient and returns their medical info</p>"


