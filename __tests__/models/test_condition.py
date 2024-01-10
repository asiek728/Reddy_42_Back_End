def test_create_condition(create_condition):
    condition = create_condition

    assert condition.patient_id == 1
    assert condition.condition_name == 'dying'
    assert condition.description == "too much swag"
    assert condition.start_date == "2000-6-21"
    assert condition.end_date == "2024-5-12"
