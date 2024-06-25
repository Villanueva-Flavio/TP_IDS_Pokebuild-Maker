function show_pop_up() {
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
    setTimeout(function() {
        document.getElementById('popup').style.opacity = '1';
        document.getElementById('overlay').style.opacity = '1';
    }, 10);
}

function hide_pop_up() {
    document.getElementById('popup').style.opacity = '0';
    document.getElementById('overlay').style.opacity = '0';
    setTimeout(function() {
        document.getElementById('popup').style.display = 'none';
        document.getElementById('overlay').style.display = 'none';
    }, 500);
}

document.getElementById('popup_open').addEventListener('click', show_pop_up);

['overlay', 'popup_close'].forEach(function(id) { 
    document.getElementById(id).addEventListener('click', hide_pop_up);
});