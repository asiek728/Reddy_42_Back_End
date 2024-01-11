# from application import db, app

# app.app_context().push()

# class Patient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     nhs_number = db.Column(db.Boolean)
#     date_of_birth = db.Column(db.Date, nullable=False, default=(2003, 3, 25)) #YMD format date_of_birth=date(2003,3,25)
#     sex = db.Column(db.String(1), nullable=False)
#     ethnicity = db.Column(db.String(100))
#     # foreign keys
#     conditions = db.relationship('Condition',backref='patient', lazy=True, cascade="all, delete")
    
#     def __init__(self, first_name, last_name, email, password, nhs_number, date_of_birth, sex, ethnicity):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#         self.nhs_number = nhs_number
#         self. date_of_birth = date_of_birth
#         self.sex = sex
#         self.ethnicity = ethnicity
    
#     def __repr__(self):
#         return f"My name is {self.first_name} {self.last_name} i was born {self.date_of_birth} and my email is {self.email}"

#     @property
#     def json(self):
#         return {
#             "id": self.id,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "email": self.email,
#             "password": self.password,
#             "nhs_number": self.nhs_number,
#             "date_of_birth": self.date_of_birth,
#             "sex": self.sex,
#             "conditions": self.conditions,
#         }


# class Condition(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
#     condition_name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(100), nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date,  default=(2003, 3, 25))

#     def __init__(self, patient_id, condition_name, description, start_date, end_date):
#         self.patient_id = patient_id
#         self.condition_name = condition_name
#         self.description = description
#         self.start_date = start_date
#         self.end_date = end_date

#     @property
#     def json(self):
#         return {
#             "id": self.id,
#             "patient_id": self.patient_id,
#             "condition_name": self.condition_name,
#             "description": self.description,
#             "start_date": self.start_date,
#             "end_date": self.end_date
#         }




# class Chat(db.Model):
#     pass 

# class GP(db.Model):
#     pass

    

