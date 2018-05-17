function validateSensor() {
    var x = document.forms["myForm"]["inputCoordenadas"].value;
    if(!isFloat(x)){
        alert("Coordinates must be filled out");
        return false;
    }
} 
function isFloat(n){
    return Number(n) === n && n % 1 !== 0;
}