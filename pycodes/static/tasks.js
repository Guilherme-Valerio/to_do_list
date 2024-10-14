document.addEventListener('DOMContentLoaded', () => {
    const addTaskForm = document.getElementById('addTaskForm');
    const taskList = document.getElementById('taskList');

    // Função para adicionar tarefa
    addTaskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('taskTitle').value;

        if (title) {
            const response = await fetch('/tasks/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ title })
            });

            if (response.ok) {
                location.reload(); // Recarrega a página para mostrar a nova tarefa
            } else {
                alert('Falha ao adicionar a tarefa');
            }
        }
    });

    // Função para atualizar tarefa
    taskList.addEventListener('click', async (e) => {
        if (e.target.classList.contains('update-task')) {
            const taskId = e.target.dataset.id;
            const newTitle = prompt('Digite o novo título:');

            if (newTitle) {
                const response = await fetch(`/tasks/update/${taskId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ title: newTitle }),
                });

                if (response.ok) {
                    location.reload(); // Recarrega a página para mostrar a tarefa atualizada
                } else {
                    alert('Falha ao atualizar a tarefa');
                }
            }
        }

        // Função para deletar tarefa
        if (e.target.classList.contains('delete-task')) {
            const taskId = e.target.dataset.id;

            const response = await fetch(`/tasks/delete/${taskId}`, {
                method: 'DELETE',
            });

            if (response.ok) {
                location.reload(); // Recarrega a página para mostrar a lista atualizada
            } else {
                alert('Falha ao deletar a tarefa');
            }
        }
    });
});


