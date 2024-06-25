function delete_pokemon_by_id(event) {
    event.preventDefault();
    
    const form = document.getElementById('delete_pokemon');
    const owner_id = form.getAttribute('data-owner-id');


    const pokemon_selected = document.getElementById('select_delete_pokemon');
    const pokemon_id = pokemon_selected.value;
    console.log('Owner ID:', owner_id);
    console.log('Pokemon ID:', pokemon_id);
    fetch(`/api/delete_pokemon/${owner_id}/${pokemon_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            console.log('Network response was not ok');
            return response.text().then(error => { throw new Error(error); });
        }
        return response.json();
    })
    .then(result => {
        // Eliminar el pokemon de la lista de opciones
        const optionToRemove = document.querySelector(`option[value="${pokemon_id}"]`);
        if (optionToRemove) {
            optionToRemove.remove();
        }
        console.log('Pokemon deleted successfully:', result.message);
    })
    .catch(error => {
        console.error('Failed to delete pokemon:', error);
    });
}

document.getElementById('delete_pokemon').addEventListener('submit', delete_pokemon_by_id);