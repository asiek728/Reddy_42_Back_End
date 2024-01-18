import pytest
from application import app, db
from application.conditions.model import Condition
from application.patients.model import Patient
from application.hereditary_conditions.model import HereditaryCondition
# Fixture 
@pytest.fixture
def client():
    
    # Create a test client to which we can make requests
    client = app.test_client()
    
    with app.app_context():
        db.session.rollback()
        db.drop_all()
        
    # Create a test database with some test data
    with app.app_context():
        # Create the database
        db.create_all()
        # Create fake data
        new_patient = Patient(first_name="Alex", last_name="Test", email="test@test.com", password="scrypt:32768:8:1$FziQurZHW63D8KxO$b29242e517474db51f24472ea864b4597641b44478e8ef739817222d46cee63087d7bd539cf79e04042642ed9de429c30a532527476776c41495b916028077b2", nhs_number="True", date_of_birth="2000-6-16", sex="m", ethnicity="White" )

        new_condition = Condition(patient_email="test@test.com", condition_name="Test", description="make a pain", start_date="2000-6-16", end_date="2000-6-16", image="True")

        # Inject it into the database
        db.session.add(new_patient, new_condition)
        db.session.commit()

    return client

