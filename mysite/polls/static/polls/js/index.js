// Abrir o Modal
var modal = document.getElementById("feedbackModal");
var btn = document.getElementById("feedbackBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

// Fechar o Modal ao clicar no 'x'
span.onclick = function() {
    modal.style.display = "none";
}

// Fechar o Modal ao clicar fora dele
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
