async function hola() {
    let response = await fetch("/myfirstapp/asincrono/");
    if (response.ok) { 
        let text = await response.text();
        alert(text);
    } else {
        alert("HTTP-Error: " + response.status);
    }
}