
window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    document.getElementById("estimado").textContent = `${params.get('nombre')} ${params.get('apellido')}`;
    document.getElementById("genero").textContent = params.get('genero');
    document.getElementById("edad").textContent = params.get('edad');
    document.getElementById("estado").textContent = params.get('estado');
};

document.getElementById("enviar").onsubmit = function(event){
    event.preventDefault();
    const marca = document.getElementById('marca').value;
    const placas = document.getElementById('placas').value;
    const modelo = document.getElementById('modelo').value;

    const queryParams = new URLSearchParams({
        marca, placas, modelo
    });

    window.location.href = 'cotizacion.html?' + queryParams.toString();
}