// Confirmación para eliminar cliente
window.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('form[action^="/eliminar/"]');
    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            if (!confirm('¿Seguro que deseas eliminar este cliente?')) {
                e.preventDefault();
            }
        });
    });
});
