
# ---------------------- Test Github Actions -----------------

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur notre API python de photos de chats !"}

def test_external_data():
    response = client.get("/external-data?limit=2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 2

def test_filtered_data():
    response = client.get("/filtered-data?limit=2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
