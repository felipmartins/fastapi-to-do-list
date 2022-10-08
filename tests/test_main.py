from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "You're on root route, please visit /docs to see all routes or /tasks to see all tasks"
    }