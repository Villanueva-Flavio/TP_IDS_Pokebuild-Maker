// Obtener referencias a los elementos del DOM

const pokemonInput = document.getElementById('pokemon_imagen_cuadrado');
const movimientosList = document.getElementById('habilidades');

// Manejar el evento de cambio en el campo de entrada del Pokémon
pokemonInput.addEventListener('change', async () => {
    const pokemonNombre = pokemonInput.value;
    const movimientos = await obtenerMovimientosPokemon(pokemonNombre);
    
    // Limpiar el datalist de movimientos
    movimientosList.innerHTML = '';

    // Llenar el datalist de movimientos con los movimientos obtenidos
    movimientos.forEach(movimiento => {
        const option = document.createElement('option');
        option.value = movimiento;
        movimientosList.appendChild(option);
    });
});

// Función para obtener los movimientos de un Pokémon desde la PokeAPI
async function obtenerMovimientosPokemon(pokemonNombre) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonNombre.toLowerCase()}`;
    try {
        const respuesta = await fetch(url);
        if (respuesta.ok) {
            const datosPokemon = await respuesta.json();
            const movimientos = datosPokemon.moves.map(movimiento => movimiento.move.name);
            return movimientos;
        } else {
            console.error(`Error: No se pudo obtener la información del Pokémon ${pokemonNombre}. Código de estado: ${respuesta.status}`);
            return [];
        }
    } catch (error) {
        console.error("Error al obtener los movimientos del Pokémon:", error);
        return [];
    }
}

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