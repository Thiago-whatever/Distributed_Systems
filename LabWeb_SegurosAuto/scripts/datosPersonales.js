document.getElementById("enviar").onsubmit = function(event){
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const genero = document.getElementById('genero').value;
    const edad = document.getElementById('edad').value;
    const estado = document.getElementById('estado').value;

    const queryParams = new URLSearchParams({
        nombre, apellido, genero, edad, estado
    });

    window.location.href = 'carro.html?' + queryParams.toString();
}
