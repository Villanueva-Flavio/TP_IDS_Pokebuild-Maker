function sort_list(lista) {
    const numeros = lista.filter(elemento => typeof elemento === 'number');
    const nulos = lista.filter(elemento => elemento === null);
    const resultado = [...numeros, ...nulos];
    return resultado;
}
function get_current_timestamp() {
    var now = new Date();
    var year = now.getFullYear();
    var month = String(now.getMonth() + 1).padStart(2, '0');
    var day = String(now.getDate()).padStart(2, '0');
    var hours = String(now.getHours()).padStart(2, '0');
    var minutes = String(now.getMinutes()).padStart(2, '0');
    var seconds = String(now.getSeconds()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

$(document).ready(function() {
    var owner_id = "{{ owner_id }}";
    var pokemones = [];

    try {
        pokemones = JSON.parse('{{ pokemons | tojson | safe }}');
    } catch (error) {
        console.error('Error parsing pokemon data:', error);
    }

    console.log('Owner ID:', owner_id);
    console.log('Pokemones:', pokemones);

    $('.select-pokemon').select2({
        tags: true,
        placeholder: "Busca a tu pokemon...",
        allowClear: true
    });
    $('#add_build_btn').on('click', function() {
    console.log('Boton de agregar pokemon presionado!');
    var build_name = $('#build_name').val().trim();
    var pokemon_ids = [null, null, null, null, null, null];

    $('.select-pokemon').each(function(index) {
        var pokemon_seleccionado = $(this).val();
        console.log('Selected Pokemon:', pokemon_seleccionado);
        if (pokemon_seleccionado) {
            var pokemon = pokemones.find(p => p.name === pokemon_seleccionado);
            if (pokemon) {
                pokemon_ids[index] = pokemon.id;
            } else {
                console.error('Could not find ID for selected Pokemon:', pokemon_seleccionado);
            }
        } else {
            console.error(`Pokemon ${index + 1} is empty!`);
        }
    });

    pokemon_ids = sort_list(pokemon_ids);

    if (pokemon_ids.length === 0 || pokemon_ids[0] === null) {
        console.error('pokemon_id_1 cannot be null or empty');
        return;
    }
    if (pokemon_ids[0] === null){
        console.error('pokemon_id_1 cannot be null or empty');
        return;
    }
    var build = {
        'owner_id': parseInt(owner_id),
        'build_name': build_name,
        'pokemon_id_1': pokemon_ids[0],
        'pokemon_id_2': pokemon_ids[1],
        'pokemon_id_3': pokemon_ids[2],
        'pokemon_id_4': pokemon_ids[3],
        'pokemon_id_5': pokemon_ids[4],
        'pokemon_id_6': pokemon_ids[5],
        'timestamp': get_current_timestamp(),
    };

    $.ajax({
        type: 'POST',
        url: '/api/add_build/',
        contentType: 'application/json',
        data: JSON.stringify(build),
        success: function(response) {
            console.log(response);
            if (response['status'] === 'success') {
                console.log('Build added successfully!');
            } else {
                console.error('Error adding build:', response);
            }
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', status, error);
        }
    });
});

    function procesar_datos() {
        var selectedOption = this.options[this.selectedIndex];
        var container = $(this).closest('.pokemon_container');

        if(selectedOption.value === ""){
            container.find('.name').html("NAME: ");
            container.find('.poke_LVL').html("LVL: ");
            container.find('.img_pokemon').attr('src', '');
            for (var i = 1; i <= 4; i++) { container.find('.poke_habilidad_' + i).html("ABILITY " + i + ": "); }
        } else {
            var id = $(selectedOption).attr('data-pokedex-id');
            while(id.length < 3) id = '0' + id;
            var photo = 'https://pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/' + id + '.png';
            container.find('.name').html('NAME: ' + $(selectedOption).attr('data-name'));
            container.find('.poke_LVL').html('LVL: ' + $(selectedOption).attr('data-level'));
            container.find('.img_pokemon').attr('src', photo);
            for (var i = 1; i <= 4; i++) { container.find('.poke_habilidad_' + i).html('ABILITY ' + i + ': ' + $(selectedOption).attr('data-ability-' + i)); }
        }
    }
    $('.select-pokemon').change(procesar_datos);

});