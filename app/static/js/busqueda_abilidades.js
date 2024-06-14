const pokemonInput = document.getElementById('pokemon_imagen_cuadrado');
const tipoImagenes = document.querySelectorAll('.posibles_tipo');

function actualizarImagenesTipos(tipos) {
    tipoImagenes.forEach((imagen, index) => {

        if (tipos[index]) {
            imagen.src = `static/images/tipos_pokemon/${tipos[index]}.png`;
            imagen.style.display = 'inline-block';
            
        } else {
            imagen.style.display = 'none';
        }
    });
}

pokemonInput.addEventListener('change', async () => {
    const pokemonNombre = pokemonInput.value.toLowerCase();
    const { movimientos, tipos } = await obtenerDatosPokemon(pokemonNombre);
    const movimientosList = document.getElementById('habilidades');
    movimientosList.innerHTML = '';

    movimientos.forEach(movimiento => {
        const option = document.createElement('option');
        option.value = movimiento;
        movimientosList.appendChild(option);
    });

    actualizarImagenesTipos(tipos);
});

async function obtenerDatosPokemon(pokemonNombre) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonNombre}`;

    try {
        const respuesta = await fetch(url);

        if (respuesta.ok) {
            const datosPokemon = await respuesta.json();
            const movimientos = datosPokemon.moves.map(movimiento => movimiento.move.name);
            const tipos = datosPokemon.types.map(type => type.type.name);
            return { movimientos, tipos };

        } else {
            console.error(`Error: No se pudo obtener la información del Pokémon ${pokemonNombre}. Código de estado: ${respuesta.status}`);
            return { movimientos: [], tipos: [] };
        }

    } catch (error) {
        console.error("Error al obtener los datos del Pokémon:", error);
        return { movimientos: [], tipos: [] };
    }
}