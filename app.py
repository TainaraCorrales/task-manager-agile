# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route("/tasks", methods=["POST"])
def criar_tarefa():
    data = request.get_json()
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": data.get("titulo"),
        "concluida": False
    }
    tarefas.append(tarefa)
    return jsonify(tarefa), 201

@app.route("/tasks", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200
