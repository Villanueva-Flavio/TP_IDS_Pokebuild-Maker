function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}
function validatePassword(password) {
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordPattern.test(password);
}

document.getElementById('register_form').addEventListener('submit', function(event) {
    event.preventDefault();
    const trainer_name = document.getElementById('trainer_name_input').value;
    const email = document.getElementById('email_input').value;
    const password = document.getElementById('password_input').value;
    const repeat_password = document.getElementById('repeat_password_input').value;
    if (password !== repeat_password) {
        console.log('Passwords do not match');
        $('#errorMensaje').text('Las contraseñas no coinciden');
        return;
    }
    if(trainer_name.trim() === '' || email.trim() === '' || password.trim() === '' || repeat_password.trim() === ''){
        console.log('Please fill all the fields');
        $('#errorMensaje').text('Por favor, rellene todos los campos');
        return;
    }
    if (!validateEmail(email)) {
        console.log('Invalid email');
        $('#errorMensaje').text('Correo electrónico inválido');
        return;
    }
    if (!validatePassword(password)) {
        console.log('Invalid password');
        $('#errorMensaje').text('Contraseña inválida');
        return;
    }


    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: trainer_name,
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.log(data.error);
        } else {
            console.log('User registered');
            window.location.href = '/';
        }
    });
});
function redirectToLogin() {
    window.location.href = '/login/';
}
