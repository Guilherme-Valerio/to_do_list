document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('token');
    
    // Função para obter as tarefas
    function getTasks() {
        fetch('/tasks', {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(response => response.json())
        .then(data => {
            // Atualiza a lista de tarefas no front-end
        });
    }

    // Função para adicionar uma nova tarefa
    document.getElementById('addTaskForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('taskTitle').value;
        const description = document.getElementById('taskDescription').value;

        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description })
        })
        .then(response => response.json())
        .then(data => {
            getTasks();
        });
    });

    getTasks(); // Carrega as tarefas ao carregar a página
});
