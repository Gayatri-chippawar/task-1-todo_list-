from flask import Blueprint, request, jsonify
from ..db import db
from ..models.task import Task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('', methods=['GET', 'OPTIONS'])
def get_tasks():
    if request.method == 'OPTIONS':
        
        return jsonify({'message': 'CORS preflight OK (GET)'}), 200

    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'name': t.name} for t in tasks])


@tasks_bp.route('', methods=['POST', 'OPTIONS'])
def add_task():
    if request.method == 'OPTIONS':
        
        return jsonify({'message': 'CORS preflight OK (POST)'}), 200

    data = request.get_json()
    new_task = Task(name=data['name'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added'}), 201


@tasks_bp.route('/<int:id>', methods=['DELETE', 'OPTIONS'])
def delete_task(id):
    if request.method == 'OPTIONS':
        
        return jsonify({'message': 'CORS preflight OK (DELETE)'}), 200

    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
