$('#login_form').on('submit', function(event){
    event.preventDefault();
    const email = $('#email_input').val();
    const password = $('#password_input').val();
    if(email.trim() === '' || password.trim() === ''){
        console.log('Please fill all the fields');
        $('#errorMensaje').text('Por favor, rellene todos los campos');
        return;
    }

    fetch('/api/login/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {(data.error)? $('#errorMensaje').text('Correo electrónico o contraseña incorrecta'): window.location.href = '/';});
});