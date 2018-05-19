function validateSensor() {
    var name = document.forms["myForm"]["nombre"].value;
    console.log(name);
    if (x == "") {
        alert("El campo ''Nombre Sensor'' es obligatorio");
        return false;
    }


    var x = document.forms["myForm"]["lat"].value;
    if (typeof (x) != "number") {
        alert("La latitud debe ser un valor entero");
        return false;
    }
    if (x > 90 || x < -90) {
        alert("La latitud debe estar entre -90 y 90");
        return false;
    }

    var x = document.forms["myForm"]["long"].value;
    if (typeof (x) != "number") {
        alert("La longitud debe ser un valor entero");
        return false;
    }
    if (x > 180 || x < -180) {
        alert("La longitud debe estar entre -180 y 180");
        return false;
    }
}