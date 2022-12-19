from main import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the Image Classifier!"

def test_classify():
    response = client.post(url = "/classify", data = json.dumps({"filepath": "Automobile #1 - test image (J).jpg"}))
    assert response.status_code == 200
    assert response.json() == {"prediction": "Automobile"}