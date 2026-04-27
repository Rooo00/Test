import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_suma(client):
    rv = client.get('/suma?a=10&b=5')
    assert rv.status_code == 200
    assert rv.get_json()['resultado'] == 15
