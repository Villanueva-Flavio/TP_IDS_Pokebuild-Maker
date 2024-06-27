$('#logout').on('click', function(){
    fetch('/logout', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'}})
    .then(response => {console.log((response.ok)? 'Logged out successfully': 'Error logging out');})
    .catch(error => {console.error('Error:', error);});
    window.location.href = '/';
});