const API_URL = "http://localhost:5000/tasks";

const form = document.getElementById("todo-form");
const alertSuccess = document.getElementById("div-alert-success");
const txtTaskTitle = document.getElementById("txtTaskTitle");
const btnText = document.getElementById("btn-text");
const btnSpinner = document.getElementById("btn-spinner");

try {
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const title = document.getElementById("txtTaskTitle").value.trim();

        if (title === "") {
            alert("Task title can't be an empty message");
            return;
        }

        btnText.className = "d-none";
        btnSpinner.className = "spinner-border";

        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        });

        txtTaskTitle.value = "";
        alertSuccess.classList.remove("d-none");
        alertSuccess.classList.add("d-block");

        btnText.className = "";
        btnSpinner.className = "spinner-border d-none";
    });
} catch (error) {
    console.log(error.message);
}