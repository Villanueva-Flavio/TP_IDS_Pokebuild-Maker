document.getElementById('poke_name').addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    if (selectedOption.value !== "") {
        document.getElementById('poke_LVL').value = selectedOption.getAttribute('data-level');
        document.getElementById('poke_habilidad_1').value = selectedOption.getAttribute('data-ability-1');
        document.getElementById('poke_habilidad_2').value = selectedOption.getAttribute('data-ability-2');
        document.getElementById('poke_habilidad_3').value = selectedOption.getAttribute('data-ability-3');
        document.getElementById('poke_habilidad_4').value = selectedOption.getAttribute('data-ability-4');
        document.getElementById('pokemon_imagen_cuadrado').value = selectedOption.getAttribute('data-pokedex-id');
    } else {
        document.getElementById('poke_LVL').value = "";
        document.getElementById('poke_habilidad_1').value = "";
        document.getElementById('poke_habilidad_2').value = "";
        document.getElementById('poke_habilidad_3').value = "";
        document.getElementById('poke_habilidad_4').value = "";
    }
});

// <script>
//     // const name = document.getElementById('editable-select')
//     function get_pokemon_data(name){
//         fetch('http://pokebuild-backend:5000/api/pokemon/${name}').then(response => {
//             if(!response.ok){
//                 throw new Error('Error de respuesta de la api');
//             }
//             number = name.
//             console.log(response.json());
//             return response.json();
//         });
//     }

// </script>