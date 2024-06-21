$(document).ready(function() {
    $('.select-pokemon').select2({
        tags: true,
        placeholder: "Busca a tu pokemon...",
        allowClear: true
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