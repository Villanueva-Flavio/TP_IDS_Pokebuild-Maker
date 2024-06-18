function delete_pokemon_by_id(event){
    event.preventDefault();
    const pokemon_selected = document.getElementById('editable-select');
    // El id del pokemon seleccionado
    const pokemon_id = pokemon_selected.value;
    // POKEMON_DELETE_ROUTE
    fetch(`/api/pokemon_delete/${pokemon_id}`, {
        method: 'POST',
        // REQUEST en formato JSON
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            console.log('Network response was not ok');
        }
        return response.json();
    })
    .then(result => {
        // Eliminar el pokemon de la lista de opciones
        const optionToRemove = document.querySelector(`option[value="${pokemon_id}"]`);
        if (optionToRemove) {
            optionToRemove.remove();
        }
        
        console.log('Pokemon deleted successfully');
    })
    .catch(error => {
        console.error('Failed to delete pokemon:', error);
    });
}

document.getElementById('delete_pokemon_form').addEventListener('submit', delete_pokemon_by_id);