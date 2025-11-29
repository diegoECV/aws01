// Animación fade-in para la tabla
window.addEventListener('DOMContentLoaded', function() {
    const box = document.querySelector('.table-box');
    box.style.opacity = 0;
    box.style.transform = 'translateY(30px)';
    setTimeout(() => {
        box.style.transition = 'opacity 0.7s, transform 0.7s';
        box.style.opacity = 1;
        box.style.transform = 'translateY(0)';
    }, 100);
    // Animación en los botones de acciones
    document.querySelectorAll('.actions button').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            btn.style.transform = 'scale(1.15)';
            btn.style.background = '#e3f0ff';
        });
        btn.addEventListener('mouseleave', function() {
            btn.style.transform = 'scale(1)';
            btn.style.background = '';
        });
    });
    // Animación en los botones superiores
    document.querySelectorAll('.add-btn, .logout-btn').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            btn.style.transform = 'scale(1.08)';
            btn.style.boxShadow = '0 4px 16px #1976d2a0';
        });
        btn.addEventListener('mouseleave', function() {
            btn.style.transform = 'scale(1)';
            btn.style.boxShadow = '';
        });
    });
});
