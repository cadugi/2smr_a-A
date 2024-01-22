var numero = 69;
var intentos = 0;

// Prompt the user to start the game
var pregunta = prompt('¿Quieres jugar a un juego?\n');

// If the user wants to play the game
if (pregunta == 'si') {
    alert('¡Muy bien empecemos!\n');
    alert('Tienes que adivinar un número que yo he elegido en caso de no adivinarlo pierdes.\n');
    alert('Empecemos (es del 0 al 100):\n');

    // While the user has not made 3 attempts
    while (intentos < 3) {
        // Get the user's guess
        var pregunta2 = parseInt(prompt('Introduce tu número'));
        intentos++;

        // Check if the guess is lower than the secret number
        if (pregunta2 < numero) {
            alert('Fallaste brother, es más grande. Suerte a la próxima (por cierto, mira detrás de ti)\n');
        // Check if the guess is higher than the secret number
        } else if (pregunta2 > numero) {
            alert('Casi, pero es más pequeño (estoy detrás tuya)\n');
        // Check if the guess is equal to the secret number
        } else if (pregunta2 === numero) {
            alert('Correcto, no sabes como me gusta el 69 🥵\n');
            // Display a saw-related image
            document.write('<img src="saw-feliz.jpg">');
            // Break the loop
            break;
        }

        // If the user has made 3 attempts
        if (intentos === 3) {
            alert('Lo siento, has perdido. El número era el ' + numero + ' has puesto triste a saw :(');
            // Display a different saw-related image
            document.write('<img src="saw-triste.jpg">');
        }
    }

// If the user wants to use a trick
} else if (pregunta == 'trucos') {
    alert ('jeje le sabes');
    // Get the user's desired secret number
    var trucos = prompt ('introduce el numero que quieres que sea la respuesta correcta');
    var numero2 = parseInt(trucos);

    // Initialize the game with the user's desired secret number
    alert('¡Muy bien empecemos!\n');
    alert('Tienes que adivinar un número que yo he elegido en caso de no adivinarlo pierdes.\n');
    alert('Empecemos (es del 0 al 100):\n');

    // While the user has not made 3 attempts
    while (intentos < 3) {
        // Get the user's guess
        var pregunta2 = parseInt(prompt('Introduce tu número'));
        intentos++;

        // Check if the guess is lower than the secret number
        if (pregunta2 < numero2) {
            alert('Fallaste brother, es más grande. Suerte a la próxima (por cierto, mira detrás de ti)\n');
        // Check if the guess is higher than the secret number
        } else if (pregunta2 > numero2) {
            alert('Casi, pero es más pequeño (estoy detrás tuya)\n');
        }
        else if (pregunta2 === numero2) {
            alert ('correcto buen numero es el ' + numero2 + 'UwU')
            break
        }
        if (intentos === 3) {
            alert('Lo siento, has perdido. El número era el ' + numero2 + ' has puesto triste a saw :(');
            // Display a different saw-related image
            document.write('<img src="saw-triste.jpg">');
        }
````}

// If the user enters an invalid input
} else {
    alert('Tú sabrás pringado\n');
    document.write('<img src=fuck-u.jpg>');
}

// If the user enters 'agustino'
while (pregunta == 'agustino') {
    document.write('<img src=agustino.jpg>');
    alert ('pero tiooooo');
    
}