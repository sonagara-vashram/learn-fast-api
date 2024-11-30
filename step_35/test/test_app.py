from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_item_valid():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Item 1"}

def test_read_item_invalid():
    response = client.get("/items/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid item ID"}
    
