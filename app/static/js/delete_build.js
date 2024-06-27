function delete_build_by_id(){
    const build_selected = document.getElementById('editable-select');
    // El id de la build seleccionada
    const build_id = build_selected.value;
    // BUILD_DELETE_ROUTE
    fetch(`/api/build_delete/${build_id}`, {
        method: 'POST'
    })
    .then(response => {
        if (!response.ok) {
            console.log('Network response was not ok');
        }
        return response.json();
    })
    .then(result => {
        // Eliminar el build de la lista de opciones
        const optionToRemove = document.querySelector(`option[value="${build_id_id}"]`);
        if (optionToRemove) {
            optionToRemove.remove();
        }
        
        console.log('Build deleted successfully');
    })
    .catch(error => {
        console.error('Failed to delete build:', error);
    });
}

document.getElementById('delete_build_btn')
.addEventListener('click', delete_build_by_id);
