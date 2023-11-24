document.addEventListener('DOMContentLoaded', function() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const loginButton = document.getElementById('loginButton');
    const loginForm = document.getElementById('loginForm');

    usernameInput.addEventListener('input', toggleLoginButton);
    passwordInput.addEventListener('input', toggleLoginButton);

    function toggleLoginButton() {
        if (usernameInput.value.trim() !== '' && passwordInput.value.trim() !== '') {
            loginButton.disabled = false;
        } else {
            loginButton.disabled = true;
        }
    }

    
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        if (!loginButton.disabled) {
            window.location.href = '../startmenu/index.html';
        }
    });
});
