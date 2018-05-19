function validaForm() {
    var x = document.forms["myForm"]["nick-name"].value;
    if(x == " ") {
        alert("Name must be filled out");
        return false;
    }

    var x = document.forms["myForm"]["contraseña"].value;
    if(x == " ") {
        alert("Password must be filled out");
        return false;
    }

    var x = document.forms["myForm"]["recontraseña"].valaue;
    if(x == " ") {
        alert("Every field must be filled out");
        return false;
    }
}