function validateSensor() {
    var name = document.forms["myForm"]["nombre"].value;
    if (name == "") {
        alert("El campo ''Nombre Sensor'' es obligatorio");
        return false;
    }
    var x = document.forms["myForm"]["lat"].value;
    if (x == "") {
        alert("Coordenadas incorrectas");
        return false;
    }
    var x = document.forms["myForm"]["long"].value;
    if (x == "") {
        alert("Coordenadas incorrectas");
        return false;
    }
}