<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form id="loginForm">
        <input type="text" id="username" name="username" placeholder="Username">
        <input type="password" id="password" name="password" placeholder="Password">
        <button type="button" onclick="login()">Login</button>
    </form>
    <script src="login.js"></script>
</body>
</html>
root@vmi1571846:/opt/api_zimbra# cat login.js
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://127.0.0.1:8000/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    });

    if (response.ok) {
        const data = await response.json();
        // Armazenar o token de acesso e redirecionar para o dashboard
        console.log('Token:', data.access_token);
        // Redirecionamento para dashboard.html, por exemplo
    } else {
        alert('Falha no login');
    }
}
