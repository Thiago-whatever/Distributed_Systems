function changeText(elementId) {
    var element=document.getElementById(elementId);
    element.innerHTML="12345678910";
 } 

 function changeImage() {
    element = document.getElementById("myimage")
    if (element.src.match("down")) {
        element.src = "images/Burro1.jpg";
    } else {
        element.src = "images/Burro2.gif";
    }
}
   
