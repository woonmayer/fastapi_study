from fastapi.testclient import TestClient
import main


def test_read_main():
    client = TestClient(main.app)
    assert client.get('/').status_code == 200


def test_read_auth_needed():
    client = TestClient(main.app)
    assert client.get('/auth_needed').status_code == 401
    assert client.get('/auth_needed', headers={
        'Authorization': f'Bearer TEST_TOKEN'
    }).status_code == 200
