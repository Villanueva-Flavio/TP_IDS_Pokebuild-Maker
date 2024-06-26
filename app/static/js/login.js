document.getElementById('login_form').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email_input').value;
    const password = document.getElementById('password_input').value;
    if(email.trim() === '' || password.trim() === ''){
        console.log('Please fill all the fields');
        $('#errorMensaje').text('Por favor, rellene todos los campos');
        return;
    }
    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.log(data.error);
            $('#errorMensaje').text('Correo electrónico o contraseña incorrecta');
        } else {
            console.log('User logged in');
        }
    });
});
function redirectToSignUp() {
    window.location.href = '/register/';
}