document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.getElementById('searchBar');
    const rectangles = document.querySelectorAll('.rectangle');

    // Escuchar eventos de entrada en la barra de búsqueda
    searchBar.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();

        // Mostrar/Ocultar divs según el término de búsqueda
        rectangles.forEach(rectangle => {
            const id = rectangle.id.toLowerCase();
            if (id.includes(searchTerm)) {
                rectangle.style.display = 'block';
            } else {
                rectangle.style.display = 'none';
            }
        });
    });
});