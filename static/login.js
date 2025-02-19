document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Login successful!") {
            window.location.href = '/dashboard';  // Redirect to user dashboard
        } else {
            alert("Invalid credentials");
        }
    })
    .catch(error => console.error('Error:', error));
});
