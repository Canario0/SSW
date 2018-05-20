function validateSensor() {
    var name = document.forms["myForm"]["nombre"].value;
    console.log(name);
    if (name == "") {
        alert("El campo ''Nombre Sensor'' es obligatorio");
        return false;
    }
}