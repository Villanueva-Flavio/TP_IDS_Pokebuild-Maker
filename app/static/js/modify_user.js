document.addEventListener('DOMContentLoaded', function() {
    const modForm = document.getElementById('mod_form');

    modForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;
        const profilePic = document.getElementById('profile-pic').files[0];

        const passwordValidation = validatePassword(password, confirmPassword);
        if (!passwordValidation.valid) {
            alert(passwordValidation.message);
            return;
        }

        const formData = new FormData();
        formData.append('username', name);
        formData.append('email', email);
        formData.append('password', password);
        formData.append('profile_picture', profilePic);

        fetch('/api/mod_user/{{ user_data.id }}', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
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

    function validatePassword(password, confirmPassword) {
        if (password !== confirmPassword) {
            return { valid: false, message: 'Passwords do not match' };
        }
        if (password.length < 8) {
            return { valid: false, message: 'Password should be at least 8 characters long' };
        }
        
        return { valid: true };
    }
<<<<<<< HEAD
});
=======
});
>>>>>>> 6257ca05da574da869c845092cb54fc3ffcfdb79
