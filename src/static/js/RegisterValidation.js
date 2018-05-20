function validaForm() {
    var x = document.forms["myForm"]["nick-name"].value;
    //console.log(x);
    if(x == "") {
        alert("Nombre inválido");
        return false
    }

    var y = document.forms["myForm"]["contraseña"].value;

    if(y == "") {
        alert("Introduzca una contraseña");
        return false;
    }

    var x = document.forms["myForm"]["recontraseña"].value;
    
    if(x != y) {
        alert("La contraseña no coincide");
        return false;
    }
}