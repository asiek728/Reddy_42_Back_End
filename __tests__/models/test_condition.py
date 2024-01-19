from application.conditions.model import Condition
from application.patients.model import Patient
import base64
import images
import unittest

def test_create_condition():
    condition = Condition("email10@email.com", "broken leg", "2reckless jumping off the curb", "2024-5-12", "2024-5-12", "/9j/4AAQSkZJRgABAQAAA" )

    assert condition.patient_email == "email10@email.com"
    assert condition.condition_name == "broken leg"
    assert condition.description == "2reckless jumping off the curb"
    assert condition.start_date == "2024-5-12"
    assert condition.end_date == "2024-5-12"
    assert condition.image == "/9j/4AAQSkZJRgABAQAAA"
    assert condition.__repr__() == f"<User {condition.patient_email}>"


from application import db, app
app.app_context().push()

def test_get_conditions_by_email():

    db.session.rollback()
    db.drop_all()
    db.create_all()

    patient1 = Patient(first_name="first_name1", last_name="last_name1", email="email10@email.com", password="password1", nhs_number="False", date_of_birth="2022-3-20", sex="M", ethnicity="White")
    patient2 = Patient(first_name="first_name2", last_name="last_name2", email="email2@email.com", password="password2", nhs_number="False", date_of_birth="2022-3-20", sex="F", ethnicity="White")

    binary_image_data = base64.b64decode(images.base64_image_data)


    condition1 = Condition(patient_email="email10@email.com", condition_name="broken leg", description="reckless jumping off the curb", start_date="2023-6-21", end_date="2024-5-12", image= binary_image_data )
    condition2 = Condition(patient_email="email10@email.com", condition_name="abdominal pain", description="pain caused by eating too much chocolate", start_date="2000-6-16", end_date="2024-5-12", image= binary_image_data)

    db.session.add(patient1)
    db.session.add(patient2)
    db.session.add(condition1)
    db.session.add(condition2)
    db.session.commit()

    existing = Condition.get_conditions_by_email("email10@email.com")

    assert len(existing) == 2
    assert existing[0].condition_name == "broken leg"
    assert existing[1].condition_name == "abdominal pain"

    nonExisting = Condition.get_conditions_by_email("nonexistent@example.com")

    assert len(nonExisting) == 0

    db.session.rollback()


class JsonTest(unittest.TestCase):
    def test_json(self):
        image_data = b'/9sc45'
        instance = Condition(
            patient_email="email10@email.com",
            condition_name="broken leg",
            description="description",
            start_date="2011-11-06",
            end_date="2011-11-06",
            image=image_data
        )
        result = instance.json

        self.assertEqual(result['patient_email'], "email10@email.com")
        self.assertEqual(result['condition_name'], "broken leg")
        self.assertEqual(result['description'], "description")
        self.assertEqual(result['start_date'], "2011-11-06")
        self.assertEqual(result['end_date'], "2011-11-06")
        self.assertIn('image_data_base64', result)
        self.assertIsNotNone(result['image_data_base64'])
