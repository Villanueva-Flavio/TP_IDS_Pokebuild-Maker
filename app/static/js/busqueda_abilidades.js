<<<<<<< HEAD
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
=======
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

>>>>>>> origin/API-modify
    movimientos.forEach(movimiento => {
        const option = document.createElement('option');
        option.value = movimiento;
        movimientosList.appendChild(option);
    });
<<<<<<< HEAD
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

$('.select-pokemon').on('change', function() {
    pokemon_id = $(this).val();

    console.log(pokemon_id);
    fetch('/api/moves/' + pokemon_id)
        .then(response => response.json())
        .then(data => {
            var move_list = data['moves'];
            console.log(move_list);
            $('#ability_1, #ability_2, #ability_3, #ability_4').each(function() {
                $(this).empty();
                $(this).append('<option value=""></option>');
                for(var i = 0; i < move_list.length; i++) {
                    $(this).append('<option value="' + move_list[i] + '">' + move_list[i] + '</option>');
                }
            });
        });

    fetch('/api/types/' + pokemon_id)
        .then(response => response.json())
        .then(data => {
            var pokemon_type = data['pokemon_type']
            var good_against = data['good_against']
            var bad_against = data['bad_against']
            console.log('Pokemon Type: ' + pokemon_type)
            console.log('Good Against: ' + good_against)
            console.log('Bad Against: ' + bad_against)

            $('.type-container img').remove();
            $('#good img').remove();
            $('#bad img').remove();

            pokemon_type.forEach(type => {
                $('.type-container').append('<img src="/static/images/tipos_pokemon/' + type + '.png" alt="type" class="img-type">')
            })

            good_against.forEach(type => {
                $('#good').append('<img src="/static/images/tipos_pokemon/' + type + '.png" alt="type" class="img-type-against">')
            })

            bad_against.forEach(type => {
                $('#bad').append('<img src="/static/images/tipos_pokemon/' + type + '.png" alt="type" class="img-type-against">')
            })

            while (pokemon_id.length < 3) { pokemon_id = '0' + pokemon_id; }

            var pokemon_image_url = 'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/' + pokemon_id + '.png';

            $('#pokemon-image').attr('src', pokemon_image_url)
        })
});
$('#add_pokemon_btn').on('click', function() {
    var pokemon_name = $('#poke_name').val();
    var pokemon_level = $('#poke_LVL').val();
    var pokemon_species = $('#pokemon_especie').val();
    var pokemon_ability_1 = $('#ability_1').val();
    var pokemon_ability_2 = $('#ability_2').val();
    var pokemon_ability_3 = $('#ability_3').val();
    var pokemon_ability_4 = $('#ability_4').val();

    fetch('/api/add_pokemon', {
        method: 'POST',
        body: JSON.stringify({
            'name': pokemon_name,
            'level': pokemon_level,
            'ability_1': pokemon_ability_1,
            'ability_2': pokemon_ability_2,
            'ability_3': pokemon_ability_3,
            'ability_4': pokemon_ability_4,
            'pokedex_id': pokemon_id,
            'owner_id': owner_id
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Respuesta del servidor:');
        console.log(data);
    })
    .catch(error => {
        console.error('Error al enviar la solicitud:', error);
    });
});
=======

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
>>>>>>> origin/API-modify
