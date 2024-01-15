import pytest
from application import create_app, db
from application.models import FriendsCharacter

@pytest.fixture
def client():
    env = "TEST"
    # Initialise a test app
    app = create_app(env)
    
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
        test_patient = Patient(first_name="test", last_name="test", email="test@email.com", password="passwordtest", nhs_number=True, date_of_birth="2001-3-4", sex="f", ethnicity="white")
        # Inject it into the database
        db.session.add(test_patient)
        db.session.commit()

    return client