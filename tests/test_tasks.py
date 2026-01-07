import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_create_task():
    client = app.test_client()
    response = client.post('/tasks', json={'title': 'Nova tarefa'})
    assert response.status_code == 201

def test_get_tasks():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
