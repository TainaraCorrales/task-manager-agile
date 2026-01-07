import json
from app import app

def test_create_task():
    client = app.test_client()
    response = client.post('/tasks', json={'title': 'Nova tarefa'})
    assert response.status_code == 201

def test_get_tasks():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
