// Validación simple para formulario de cliente
window.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-box');
    form.addEventListener('submit', function(e) {
        const dni = form.querySelector('input[name="dni_ruc"]').value.trim();
        const nombres = form.querySelector('input[name="nombres"]').value.trim();
        if (!dni || !nombres) {
            alert('DNI/RUC y Nombres son obligatorios.');
            e.preventDefault();
        }
    });
});
