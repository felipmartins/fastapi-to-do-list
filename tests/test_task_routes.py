from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_tasks_route():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_post_task_route_without_body_content():
    response = client.post("/tasks")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


def test_post_task_route_with_body_content():
    response = client.post("/tasks", json={"id":100000000000000000, "title": "string", "description": "string"})
    assert response.status_code == 201
    assert 'created' in response.json()


def test_put_task_route_without_body_content():
    response = client.put("/tasks/5")
    assert response.status_code == 422
    assert "body" in response.json()['detail'][0]['loc']
    assert "field required" in response.json()['detail'][0]['msg']
    assert "value_error.missing" in response.json()['detail'][0]['type']


def test_put_task_route_with_body_content():
    response = client.put("/tasks/100000000000000000", json={ "title": "string_editada", "description": "string_editada"})
    assert response.status_code == 200
    assert 'edited' in response.json()


def test_delete_task_route():
    response = client.delete("/tasks/100000000000000000")
    assert response.status_code == 200
    assert 'deleted' in response.json()


def test_method_not_allowed():
    response = client.put("/tasks")
    assert response.status_code == 405
    assert "method not allowed" in response.json()['detail'].lower()