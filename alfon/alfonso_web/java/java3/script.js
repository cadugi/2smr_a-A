var numero = 69
var pregunta = prompt('quieres jugar a un juego?')

if (pregunta == 'si') {
    alert('muy bien empecemos')
    alert('tienes que adivinar un número que yo he elegido en caso de no adivinarlo pierdes.')
    alert('empecemos (es del 0 al 100):')
    var pregunta2 = parseInt(prompt('introduce tu número'))

    if (pregunta2 < numero) {
        alert('fallaste brother es más grande, suerte a la próxima (por cierto, mira detrás de ti)')
        document.write ('<img src="saw-triste.jpg">')
    } else if (pregunta2 > numero) {
        alert('casi, pero es más pequeño (estoy detrás tuya)')
        document.write ('<img src="saw-triste.jpg">')
    } else if (pregunta2 === numero) {
        alert('correcto, no sabes como me gusta el 69 🥵')
        document.write ('<img src="saw-feliz.jpg">')
    }
}
    
else
    {
        alert('tu sabras pringado')
        document.write ('<img src=fuck-u.jpg>')
    }

