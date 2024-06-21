const pokemonInput = document.getElementById('pokemon_especie');
const tipoImagenes = document.querySelectorAll('.posibles_tipo');
const goodAgainstContainer = document.querySelector('.good_against div');
const badAgainstContainer = document.querySelector('.bad_against div');

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

function actualizarGoodAgainst(goodAgainst) {
    goodAgainstContainer.innerHTML = '';

    goodAgainst.forEach(tipo => {
        const img = document.createElement('img');
        img.src = `static/images/tipos_pokemon/${tipo}.png`;
        img.classList.add('tipo_imagen', 'tipo_pokemon_Good_Against');
        goodAgainstContainer.appendChild(img);
    });
}

function actualizarBadAgainst(badAgainst) {
    badAgainstContainer.innerHTML = '';

    badAgainst.forEach(tipo => {
        const img = document.createElement('img');
        img.src = `static/images/tipos_pokemon/${tipo}.png`;
        img.classList.add('tipo_imagen', 'tipo_pokemon_Bad_Against');
        badAgainstContainer.appendChild(img);
    });
}

pokemonInput.addEventListener('change', async () => {
    const pokemonNombre = pokemonInput.value.toLowerCase();
    const { movimientos, tipos, good_against, bad_against } = await obtenerDatosPokemon(pokemonNombre);
    const movimientosList = document.getElementById('habilidades');
    movimientosList.innerHTML = '';

    movimientos.forEach(movimiento => {
        const option = document.createElement('option');
        option.value = movimiento;
        movimientosList.appendChild(option);
    });

    actualizarImagenesTipos(tipos);
    actualizarGoodAgainst(good_against);
    actualizarBadAgainst(bad_against);
});

async function obtenerDatosPokemon(pokemonNombre) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonNombre}`;

    try {
        const respuesta = await fetch(url);

        if (respuesta.ok) {
            const datosPokemon = await respuesta.json();
            const movimientos = datosPokemon.moves.map(movimiento => movimiento.move.name);
            const tipos = datosPokemon.types.map(type => type.type.name);
            const url_tipos = datosPokemon.types.map(type => type.type.url);

            let good_against = new Set();
            let bad_against = new Set();

            for (let url of url_tipos) {
                const datos = await fetch(url);

                if (datos.ok) {
                    const datosTipos = await datos.json();
                    const buenos_contra = datosTipos.damage_relations.double_damage_to.map(tipo => tipo.name);

                    for (let tipo of buenos_contra) {
                        good_against.add(tipo);
                    }

                    const malos_contra = datosTipos.damage_relations.double_damage_from.map(tipo => tipo.name);

                    for (let tipo of malos_contra) {
                        bad_against.add(tipo);
                    }
                }
            }

            good_against = [...good_against];
            bad_against = [...bad_against];

            return { movimientos, tipos, good_against, bad_against };

        } else {
            console.error(`Error: No se pudo obtener la información del Pokémon ${pokemonNombre}. Código de estado: ${respuesta.status}`);
            return { movimientos: [], tipos: [], good_against: [], bad_against: [] };
        }

    } catch (error) {
        console.error("Error al obtener los datos del Pokémon:", error);
        return { movimientos: [], tipos: [], good_against: [], bad_against: [] };
    }
}
