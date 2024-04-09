
window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    document.getElementById("estimado").textContent = `${params.get('nombre')} ${params.get('apellido')}`;
    document.getElementById("genero").textContent = params.get('genero');
    document.getElementById("edad").textContent = params.get('edad');
    document.getElementById("estado").textContent = params.get('estado');
    document.getElementById("marca").textContent = params.get('marca');
    document.getElementById("modelo").textContent = params.get('modelo');
    document.getElementById("placas").textContent = params.get('placas');
};
