function delete_pokemon_by_id(){
    const pokemon_selected = document.getElementById('editable-select');
    // El id del pokemon seleccionado
    const pokemon_id = pokemon_selected.value;
    // POKEMON_DELETE_ROUTE
    fetch(`/api/pokemon_delete/${pokemon_id}`, {
        method: 'POST'
    })
    .then(response => {
        return response.json();
    })
    .then(result => {
        console.log('Pokemon deleted successfully');
    })
}

document.getElementById('delete_pokemon_btn')
.addEventListener('click', delete_pokemon_by_id);