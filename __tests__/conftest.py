import pytest
from application import app
from application.models import Condition

@pytest.fixture()
def create_condition():
    condition = Condition(1, "dying", "too much swag", "2000-6-21", "2024-5-12")
    return condition
