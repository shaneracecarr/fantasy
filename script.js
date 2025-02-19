document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevents page refresh
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username === "admin" && password === "password") {
        document.getElementById("message").textContent = "Login successful!";
        document.getElementById("message").style.color = "green";
        // Redirect or store login state later
    } else {
        document.getElementById("message").textContent = "Invalid login!";
        document.getElementById("message").style.color = "red";
    }
});
