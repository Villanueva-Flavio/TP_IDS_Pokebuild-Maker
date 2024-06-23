document.querySelectorAll('.build-container').forEach(container => {
    container.addEventListener('click', function() {
        const buildName = this.querySelector('.build-name-container').textContent;
        const pokemonIds = [
            this.querySelector('.pokemon1').style.backgroundImage,
            this.querySelector('.pokemon2').style.backgroundImage,
            this.querySelector('.pokemon3').style.backgroundImage,
            this.querySelector('.pokemon4').style.backgroundImage,
            this.querySelector('.pokemon5').style.backgroundImage,
            this.querySelector('.pokemon6').style.backgroundImage
        ];

        document.getElementById('build-details-name').textContent = buildName;

        const buildDetailsPokemons = document.getElementById('build-details-pokemons');
        buildDetailsPokemons.innerHTML = '';

        pokemonIds.forEach(pokemon => {
            const div = document.createElement('div');
            div.classList.add('pokemon');
            const url = pokemon.slice(5, -2);
            div.style.backgroundImage = `url(${url})`;
            buildDetailsPokemons.appendChild(div);
        });
    });
});
