from main import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Intro": "Welcome to the Image Classifier!"}

def test_classify():
    response = client.post(url = "/classify", data = json.dumps({"filepath": "images/Automobile #1.jpg"}))
    assert response.status_code == 200
    assert response.json() == {"prediction": "Automobile"}