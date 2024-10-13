from flask import Flask, make_response, jsonify, request
from db import Tasks

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    return make_response(
        jsonify(Tasks), 200
    )

@app.route('/tasks', methods = ['POST'])
def post_tasks():
    task = request.json
    
    if not task or not 'Título' in task or not 'Descrição' in task:
        return make_response(jsonify({"erro": "Dados inválidos"}), 400)
    
    Tasks.append(task)
    return make_response(jsonify(Tasks), 201)



@app.route('/tasks/<int:task_index>', methods=['PUT', 'DELETE']) 
def manage_task(task_index):
    if request.method == 'PUT':
        task_data = request.json
        if task_index >= len(Tasks) or task_index < 0:
            return jsonify({"erro": "Tarefa não encontrada"}), 404
        Tasks[task_index] = task_data
        return jsonify(Tasks[task_index]), 200
    
    if request.method == 'DELETE':
        if task_index >= len(Tasks) or task_index < 0:
            return jsonify({"erro": "Tarefa não encontrada"}), 404
        removed_task = Tasks.pop(task_index)
        return jsonify(removed_task), 200
    
    
if __name__ == "__main__":
    app.run(debug=True)