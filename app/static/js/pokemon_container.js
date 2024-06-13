const name = document.getElementById('editable-select')
function get_pokemon_data (){
    fetch(f'http://pokebuild-backend:5000/api/pokemon/{user_id}')
}