function validateForm() {
    var x = document.forms["myForm"]["nick-name"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }

    var x = document.forms["myForm"]["contraseña"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
}