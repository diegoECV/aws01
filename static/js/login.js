// Validación simple para login
window.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.login-box');
    form.addEventListener('submit', function(e) {
        const username = form.querySelector('input[name="username"]').value.trim();
        const password = form.querySelector('input[name="password"]').value.trim();
        if (!username || !password) {
            alert('Por favor, ingrese usuario y contraseña.');
            e.preventDefault();
        }
    });
});
