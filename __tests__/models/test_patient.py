from application.patients.model import Patient, generate_uuid, TokenBlocklist
from application.hereditary_conditions.model import HereditaryCondition
from uuid import uuid4
import unittest
from werkzeug.security import generate_password_hash, check_password_hash

def test_create_patient():
    new_patient = Patient(first_name="first_name", last_name="last_name", email="email@email.com", password="password", nhs_number="False", date_of_birth="2024-5-12", sex="M", ethnicity="White")

    assert new_patient.first_name == "first_name"
    assert new_patient.last_name == "last_name"
    assert new_patient.email == "email@email.com"
    assert new_patient.password == "password"
    assert new_patient.nhs_number == "False"
    assert new_patient.date_of_birth == "2024-5-12"
    assert new_patient.sex == "M"
    assert new_patient.ethnicity == "White"
    assert new_patient.__repr__() == f"<User {new_patient.first_name}>"


class unit_tests(unittest.TestCase):
    def setUp(self):
        self.patient = Patient(first_name="first_name", last_name="last_name", email="email@email.com", password="password", nhs_number="False", date_of_birth="2024-5-12", sex="M", ethnicity="White")

        self.condition1 = HereditaryCondition(email="email@email.com", hereditary_condition_name="Condition1")
        self.condition2 = HereditaryCondition(email="email@email.com", hereditary_condition_name="Condition2")

    def test_generate_uuid(self):
        result = generate_uuid()
        self.assertIsInstance(result, uuid4)

    def test_set_password(self):
        password = "password"
        self.patient.set_password(password)
        self.assertIsNotNone(self.patient.password)
        self.assertTrue(self.patient.password.startswith("scrypt:32768"))

    def test_check_password(self):
        password = "password"
        hashed_password = generate_password_hash(password)
        self.patient.password = hashed_password
        self.assertTrue(self.patient.check_password(password))

    def test_json(self):
        self.patient.hereditary_conditions.append(self.condition1)
        self.patient.hereditary_conditions.append(self.condition2)
        result = self.patient.json

        self.assertEqual(result['first_name'], "first_name")
        self.assertEqual(result['last_name'], "last_name")
        self.assertIsInstance(result['hereditary_conditions'], list)
        self.assertEqual(len(result['hereditary_conditions']), 2)
        self.assertEqual(result['hereditary_conditions'][0]['hereditary_condition_name'], "Condition1")
        self.assertEqual(result['hereditary_conditions'][1]['hereditary_condition_name'], "Condition2")


def test_create_TokenBlocklist():
    new_token = TokenBlocklist(jti="jti", create_at="2024-5-12")

    assert new_token.jti == "jti"
    assert new_token.create_at == "2024-5-12"
    assert new_token.__repr__() == f"<Token {new_token.jti}>"

from application import db, app
app.app_context().push()
def test_get_user_by_email():

    db.session.rollback()
    db.drop_all()
    db.create_all()

    patient1 = Patient(first_name="first_name1", last_name="last_name1", email="email10@email.com", password="password1", nhs_number="False", date_of_birth="2022-3-20", sex="M", ethnicity="White")
    patient2 = Patient(first_name="first_name2", last_name="last_name2", email="email2@email.com", password="password2", nhs_number="False", date_of_birth="2022-3-20", sex="F", ethnicity="White")

    db.session.add(patient1)
    db.session.add(patient2)
    db.session.commit()

    existing = Patient.get_user_by_email("email10@email.com")
    assert existing.first_name == "first_name1"
    db.session.rollback()



#pipenv run coverage
