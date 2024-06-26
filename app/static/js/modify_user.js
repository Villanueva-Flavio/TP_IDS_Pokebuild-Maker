
function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}
function validatePassword(password) {
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordPattern.test(password);
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('mod_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirm_password = document.getElementById('confirm-password').value;
        const profile_pic = document.getElementById('profile-pic').files[0];

        
        const passwordValidation = validatePassword(password, confirm_password);
        if (!passwordValidation.valid) {
            alert(passwordValidation.message);
            return;
        }

        const formData = new FormData();
        formData.append('username', name);
        formData.append('email', email);
        formData.append('password', password);
        formData.append('profile_picture', profile_pic);
        if(username.trim() === "" || email.trim() === "" || password.trim() === ""){
            $("#errorMensaje").html("Rellenar todos los campos");
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

        fetch('/api/mod_user/{{ user_data.id }}', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                window.location.href = '/user_profile/{{ user_data.id }}';
            } else {
                alert(data.message || 'Failed to update profile');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to update profile');
        });
    });
});

function validatePassword(password, confirmPassword) {
    if (password !== confirmPassword) {
        return { valid: false, message: 'Passwords do not match' };
    }
    if (password.length < 8) {
        return { valid: false, message: 'Password should be at least 8 characters long' };
    }
    

    return { valid: true };
}
