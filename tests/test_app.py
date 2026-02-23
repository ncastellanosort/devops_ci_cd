from src.app import app

def test_home_status_code_200_ok():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200

def test_home_response_hello_devops():
    client = app.test_client()
    resp = client.get("/")
    assert resp.get_json() == {"message": "Hello DevOps, this is a full cicle explaination (CI/CD)."}
