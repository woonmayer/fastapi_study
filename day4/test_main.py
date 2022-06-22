from fastapi.testclient import TestClient
import main

def test_read_main():
    client = TestClient(main.app)
    assert client.get('/').status_code == 200
