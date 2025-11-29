// Animación fade-in para el login
window.addEventListener('DOMContentLoaded', function() {
    const box = document.querySelector('.login-box');
    box.style.opacity = 0;
    box.style.transform = 'scale(0.95)';
    setTimeout(() => {
        box.style.transition = 'opacity 0.7s, transform 0.7s';
        box.style.opacity = 1;
        box.style.transform = 'scale(1)';
    }, 100);
    // Animación en el botón
    const btn = box.querySelector('button');
    btn.addEventListener('mouseenter', function() {
        btn.style.transform = 'scale(1.05)';
        btn.style.boxShadow = '0 4px 16px #1976d2a0';
    });
    btn.addEventListener('mouseleave', function() {
        btn.style.transform = 'scale(1)';
        btn.style.boxShadow = '';
    });
});
