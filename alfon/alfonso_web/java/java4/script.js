var años = prompt('cuantos años tienes');
if (años >= 0 && años <= 3) {
    alert ('tienes menos de 3 años')
}
else if (años >= 4 && años <= 17){
    alert ('tienes menos de 18 pero mas de de 4')
}
else if (años >= 18) {
    alert ('tienes mas de 18')
}
else {
    alert ('introduce un numero valido')
}