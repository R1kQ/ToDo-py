const API_URL = "http://localhost:5000/tasks"

async function loadTodos(params) {
    const response = await fetch("/tasks");
    const todos = await response.json();
    const todoList = document.getElementById("div-todos");
    todoList.innerHTML = "";

    todos.forEach(todo => {
        const div = document.createElement("div");
        div.className = "todo-item col-xs-12 col-sm-6 col-md-4 col-lg-4 p-3 bg-light shadow border";

        if (todo.complete !== true) {
            div.innerHTML = `
                        <p class="h4 mb-3">${todo.title}</p>
                        <button class="btn btn-success not-completed w-25 shadow-sm" onclick="updateTodo(${todo.id}, ${true})">Complete</button>
                        `;
        } else {
            div.innerHTML = `
                        <p class="h4 mb-3">${todo.title}</p>
                        <button class="btn btn-secondary w-25 shadow-sm completed">Completed</button>
                        `;
        }

        todoList.appendChild(div);
    });
}

async function updateTodo(id, complete) {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ complete })
    });

    if (response.ok) {
        await loadTodos();
    }
}

window.onload = loadTodos;