
window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    document.getElementById("estimado").textContent = `${params.get('nombre')} ${params.get('apellido')}`;
    document.getElementById("genero").textContent = params.get('genero');
    document.getElementById("edad").textContent = params.get('edad');
    document.getElementById("estado").textContent = params.get('estado');
    console.log(params.toString());

};

document.addEventListener('DOMContentLoaded', function () {
    // Ahora asignamos el evento onsubmit al formulario en lugar del botón.
    document.getElementById("formularioAuto").onsubmit = function(event) {
        event.preventDefault(); // Esto previene que el formulario se envíe.

        const marca = document.getElementById('marca').value;
        const placas = document.getElementById('placas').value;
        const modelo = document.getElementById('modelo').value;

        // Ahora puedes ver los valores en alertas o en la consola

        const existingParams = new URLSearchParams(window.location.search);

        existingParams.set('marca', marca);
        existingParams.set('placas', placas);
        existingParams.set('modelo', modelo);

        // Si quieres redireccionar con los parámetros nuevos, hazlo aquí
        window.location.href = 'cotizacion.html?' + existingParams.toString();
    };
});