function submitForm(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // In a real-world scenario, you would make an AJAX request to the server to validate the credentials.
    // For simplicity, we'll just check if the username is "user" and the password is "password".
    if (username === 'user' && password === 'password') {
        window.location.href = 'dashboard.html'; // Redirect to the dashboard
    } else {
        document.getElementById('error-message').innerText = 'Invalid username or password';
    }
}
