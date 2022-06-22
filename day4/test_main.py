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


def test_path_param():
    client = TestClient(main.app)
    path_param = 'TEST_VALUE'
    assert client.get(f'/path_param/{path_param}').json() == path_param


def test_query_param():
    client = TestClient(main.app)
    query_param = 'TEST_VALUE'
    assert client.get(f'/query_param?q={query_param}').json()['q'] == query_param


def test_body():
    client = TestClient(main.app)
    product = {
            'name': 'GOOD',
            'code': 'ABCD'
    }
    option = {
            'name': 'A',
    }
    assert client.post(f'/product', json={
        'product': product, 'option': option
    }).json() == [product, option]
