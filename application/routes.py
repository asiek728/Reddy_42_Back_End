from application import app, db
from flask import request, jsonify, render_template, redirect

# from application.patients.model import Patient

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

@app.route('/testing')
def testing():
    return {"test1": ['The test has worked!']}
 


# @app.route('/add_dummy_data')
# def dummy():~
#formatting------------------------------------------------------------------------------------------------------
# def format_patient(patient):
#     return {
#         'first_name': patient.first_name,
#         'last_name': patient.last_name,
#         'email': patient.email,
#         'password':patient.password,
#         'nhs_number': patient.nhs_number,
#         'date_of_birth': patient.date_of_birth,
#         'sex': patient.sex,
#         'ethnicity': patient.ethnicity
#     }

# def format_condition(condition):
#     return {
#         'patient_id ': condition.patient_id ,
#         'condition_name': condition.condition_name,
#         'description': condition.description,
#         'start_date': condition.start_date,
#         'end_date': condition.end_date,
#     }

#patient route----------------------------------------------------------------------------------------------------

# @app.route("/patients/<id>") #WORKING!
# def get_patient_info(id):
#     patient = Patient.query.filter_by(id=id).first()
#     return jsonify(format_patient(patient))

# @app.route("/patients", methods=['POST']) #WORKING!
# def create_patient():
#     data = request.json
#     patient = Patient(data['first_name'], data['last_name'], data['email'], data['password'], data['nhs_number'], data['date_of_birth'], data['sex'], data['ethnicity'])
#     db.session.add(patient)
#     db.session.commit()
#     return f"{patient} added succesfully"

# @app.route("/patients/<id>", methods=['PATCH']) #WORKING!
# def update_patient(id):
#     patient = Patient.query.filter_by(id=id)
#     data = request.json
#     patient.update(dict(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'], nhs_number=data['nhs_number'], date_of_birth=data['date_of_birth'], sex=data['sex'], ethnicity=data['ethnicity']))
#     db.session.commit()
#     updatedPatient = patient.first() 
#     return jsonify(format_patient(updatedPatient))

# @app.route("/patients/<id>", methods=['DELETE']) #WORKING!
# def destroy_patient(id):
#     patient = Patient.query.filter_by(id=id).first()
#     db.session.delete(patient)
#     db.session.commit()
#     return f"Patient deleted {id}"

#condition routes-----------------------------------------------------------------------------------------------------

# @app.route("/condition") #WORKING!
# def get_conditions():
#     conditions = Condition.query.all()
#     print(conditions)
#     condition_list = []
#     for condition in conditions:
#         condition_list.append(format_condition(condition))
#     return jsonify(condition_list)

# @app.route("/condition/<id>") #WORKING!
# def get_condition_by_id(id):
#     condition = Condition.query.filter_by(id=id).first()
#     return jsonify(format_condition(condition))

# @app.route("/condition", methods=["POST"]) #WORKING!
# def create_condition():
#     data = request.json
#     condition = Condition(data['patient_id'], data['condition_name'], data['description'], data['start_date'], data['end_date'])
#     db.session.add(condition)
#     db.session.commit()
#     return jsonify(format_condition(condition))

# @app.route("/condition/<id>", methods=["PATCH"]) #WORKING!
# def update_condition(id):
#     condition = Condition.query.filter_by(id=id)
#     data = request.json
#     condition.update(dict(patient_id=data['patient_id'], condition_name=data['condition_name'], description=data['description'],start_date=data['start_date'], end_date=data['end_date']))
#     db.session.commit()
#     updatedCondition = condition.first() 
#     return jsonify(format_condition(updatedCondition))

# @app.route("/condition/<id>", methods=['DELETE'])
# def destroy_condition(id):
#     condition = Condition.query.filter_by(id=id).first()
#     db.session.delete(condition)
#     db.session.commit()
#     return f"Condition deleted {id}"

#chat routes----------------------------------------------------------------------------------------------------------


#diagnosis routes-----------------------------------------------------------------------------------------------------
