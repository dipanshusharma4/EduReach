function login() {
    document.getElementById("login").style.display = "flex";
    document.getElementById("register").style.display = "none";
    document.getElementById("btn").style.left = "0";
}

function register() {
    document.getElementById("login").style.display = "none";
    document.getElementById("register").style.display = "flex";
    document.getElementById("btn").style.left = "50%";
}
