let años = prompt('cuantos años tienes');
let mensaje =
    años >= 0 && años <= 3
    ? alert("tu edad esta entre 0 y 3")
    : años >= 4 && años <= 17
    ? alert("tu edad es mayor a 3 pero menor o igual a 17")
    : años >= 18 && 130
    ? alert("tienes mas de 18")
    :console.log(mensaje);