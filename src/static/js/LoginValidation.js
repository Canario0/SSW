function validateForm() {
    var x = document.forms["myForm"]["nick-name"].value;

    if (x == "") {
        alert("Nombre inválido");
        return false;
    }

    var x = document.forms["myForm"]["contraseña"].value;

    if (x == "") {
        alert("Contraseña incorrecta");
        return false;
    }
}