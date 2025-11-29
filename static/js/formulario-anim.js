// Animación fade-in para el formulario
window.addEventListener('DOMContentLoaded', function() {
    const box = document.querySelector('.form-box');
    box.style.opacity = 0;
    box.style.transform = 'translateY(30px)';
    setTimeout(() => {
        box.style.transition = 'opacity 0.7s, transform 0.7s';
        box.style.opacity = 1;
        box.style.transform = 'translateY(0)';
    }, 100);
    // Animación en el botón
    const btn = box.querySelector('button');
    btn.addEventListener('mouseenter', function() {
        btn.style.transform = 'scale(1.05)';
        btn.style.boxShadow = '0 4px 16px #388e3ca0';
    });
    btn.addEventListener('mouseleave', function() {
        btn.style.transform = 'scale(1)';
        btn.style.boxShadow = '';
    });
});
