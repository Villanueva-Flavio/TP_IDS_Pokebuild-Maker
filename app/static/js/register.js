document.getElementById('register_form').addEventListener('submit', function(event) {
    event.preventDefault();
    const trainer_name = document.getElementById('trainer_name_input').value;
    const email = document.getElementById('email_input').value;
    const password = document.getElementById('password_input').value;
    const repeat_password = document.getElementById('repeat_password_input').value;
    if (password !== repeat_password) {
        console.log('Passwords do not match');
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
        }
    });
});
function redirectToLogin() {
    window.location.href = '/login/';
}