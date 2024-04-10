
window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    document.getElementById("estimado").textContent = `${params.get('nombre')} ${params.get('apellido')}`;
    document.getElementById("genero").textContent = params.get('genero');
    document.getElementById("edad").textContent = params.get('edad');
    document.getElementById("estado").textContent = params.get('estado');
    document.getElementById("marca").textContent = params.get('marca');
    document.getElementById("modelo").textContent = params.get('modelo');
    document.getElementById("placas").textContent = params.get('placas');

    //Incluir cotizacion (randomizar)
    // Generar un número aleatorio entre 0 y 10000
    const cotizacion = Math.floor(Math.random() * 10001);

    // Crear un párrafo para mostrar la cotización
    const pCotizacion = document.createElement("p");
    pCotizacion.textContent = `USD $ ${cotizacion.toLocaleString()}`;

    // Seleccionar el elemento después del cual queremos insertar la cotización
    const seccionCotizacion = document.querySelector("section:nth-of-type(2)");

    // Insertar la cotización en el HTML
    seccionCotizacion.appendChild(pCotizacion);

};
