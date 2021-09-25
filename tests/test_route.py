import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_default_route(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_service_bad_http_method(client):
    resp = client.get('/predict')
    assert resp.status_code == 405