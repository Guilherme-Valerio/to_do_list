from flask import Blueprint, jsonify, request
from app import db
from models import Task
from flask_jwt_extended import jwt_required

task_routes = Blueprint('tasks', __name__)

# Rota GET - Listar todas as tarefas
@task_routes.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
    return jsonify(task_list), 200

# Rota POST - Adicionar uma nova tarefa
@task_routes.route('/tasks', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully!'}), 201

# Rota DELETE - Remover uma tarefa
@task_routes.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully!'}), 200

# Rota PUT - Atualizar uma tarefa
@task_routes.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data['title']
    task.description = data.get('description')
    db.session.commit()
    return jsonify({'message': 'Task updated successfully!'}), 200
