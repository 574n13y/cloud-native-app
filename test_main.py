from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "version": "1.0.0"
    }

def test_create_task():
    task_data = {
        "title": "Test Task",
        "description": "Test Description"
    }
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert "id" in data
    assert "created_at" in data

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    # First create a task
    task_data = {
        "title": "Task to Delete",
        "description": "This task will be deleted"
    }
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    
    # Then delete it
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    
    # Verify it's deleted
    get_response = client.get("/tasks")
    tasks = get_response.json()
    assert not any(task["id"] == task_id for task in tasks)
