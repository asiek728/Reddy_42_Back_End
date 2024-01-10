from application import db, app

app.app_context().push()

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nhs_number = db.Column(db.Boolean)
    date_of_birth = db.Column(db.Date, nullable=False, default=(2003, 3, 25)) #YMD format date_of_birth=date(2003,3,25)
    sex = db.Column(db.String(1), nullable=False)
    ethnicity = db.Column(db.String(100))
    # foreign keys
    conditions = db.relationship('Condition',backref='patient', lazy=True, cascade="all, delete")
    
    def __init__(self, first_name, last_name, email, password, nhs_number, date_of_birth, sex, ethnicity):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.nhs_number = nhs_number
        self. date_of_birth = date_of_birth
        self.sex = sex
        self.ethnicity = ethnicity
    
    def __repr__(self):
        return f"My name is {self.first_name} {self.last_name} i was born {self.date_of_birth} and my email is {self.email}"

    @property
    def json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "nhs_number": self.nhs_number,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "conditions": self.conditions,
        }
