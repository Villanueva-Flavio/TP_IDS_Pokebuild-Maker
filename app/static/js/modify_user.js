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

        if (name.trim() === '' || email.trim() === '') {
            alert('Name and email are required fields.');
            return;
        }

        const formData = new FormData();
        formData.append('username', name);
        formData.append('email', email);
        formData.append('password', password);
        
        
        if (profile_pic) {
            formData.append('profile_picture', profile_pic);
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
