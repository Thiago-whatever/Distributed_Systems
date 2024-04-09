
window.onload = function () {
    const params = new URLSearchParams(window.location.search);    console.log(params);

    
    document.getElementById("estimado").textContent = `${params.get('nombre')} ${params.get('apellido')}`;
    document.getElementById("genero").textContent = params.get('genero');
    document.getElementById("edad").textContent = params.get('edad');
    document.getElementById("estado").textContent = params.get('estado');

    
};

