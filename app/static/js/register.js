function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

function validatePassword(password) {
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordPattern.test(password);
}

async function uploadImage(formData) {
    try {
        const response = await fetch('https://api.imgbb.com/1/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        if (data.success) {
            return data.data.url;
        } else {
            throw new Error('Image upload failed');
        }
    } catch (error) {
        console.error('Error uploading image', error);
        return null;
    }
}

document.getElementById('register_form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const trainer_name = document.getElementById('trainer_name_input').value;
    const email = document.getElementById('email_input').value;
    const password = document.getElementById('password_input').value;
    const repeat_password = document.getElementById('repeat_password_input').value;
    var formData = new FormData();
    formData.append('key', '00b570da421a137379a923f7292c19d7');
    formData.append('image', $('#profile_picture_input')[0].files[0]);

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
    
    const image_url = await uploadImage(formData);
    
    if (!image_url) {
        console.log('Error(1) uploading image');
        $('#errorMensaje').text('Error subiendo la imagen');
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
            password: password,
            profile_picture: image_url
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
