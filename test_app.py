import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hent_produkter(client):
    response = client.get('/api/produkter')
    assert response.status_code == 200

def test_hent_enkelt_produkt(client):
    response = client.get('/api/produkter/1')
    assert response.status_code == 200

def test_produkt_ikke_fundet(client):
    response = client.get('/api/produkter/999')
    assert response.status_code == 404
