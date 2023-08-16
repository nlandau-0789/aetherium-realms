var usernameInput = document.getElementById("username");
var passwordInput = document.getElementById("password");
var submitButton = document.getElementById("submit");

function checkFields() {
    if (usernameInput.value && passwordInput.value) {
        submitButton.disabled = false
    } else {
        submitButton.disabled = true
    }
}

usernameInput.addEventListener("input", checkFields);
passwordInput.addEventListener("input", checkFields);

checkFields()