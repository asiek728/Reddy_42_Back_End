import json

def test_index_page(client):
    response = client.get("/")
    print(response.data)
    assert response.status_code == 200
    assert response.data == b"<p>Welcome to the back end!</p>"
    
# def test_patients_page(client):
#     response = client.get("/patients")
#     assert response.status_code == 200
#     data = json.loads(response.data)
    
#     # assert data.first_name == 'Alex'
#     # assert data[0]['last_name'] == 'Test'
#     # assert data['email'] == "test@test.com"
#     # assert data[0]['password'] == "scrypt:32768:8:1$FziQurZHW63D8KxO$b29242e517474db51f24472ea864b4597641b44478e8ef739817222d46cee63087d7bd539cf79e04042642ed9de429c30a532527476776c41495b916028077b2"
#     # assert data[0]['nhs_number'] =='True'
#     # assert data[0]['date_of_birth'] == '2000-6-16'
#     # assert data[0]['sex'] == 'm'
#     # assert data[0]['ethnicity'] == "White"

def test_conditions_page(client):
    response = client.get("/conditions")
    assert response.status_code == 200
    data = json.loads(response.data)
