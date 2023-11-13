import random
from palabras_personalizadas import palabras_personalizadas

# Elige una palabra aleatoria de la lista
palabra_objetivo = random.choice(palabras_personalizadas)

# Inicializa las variables para el juego
intentos = 0
max_intentos = 10
letras_adivinadas = []

# Función para mostrar el estado actual del juego
def mostrar_estado():
    palabra_mostrada = ""
    for letra in palabra_objetivo:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    print("\nPalabra: " + palabra_mostrada)
    print("Intentos restantes:", max_intentos - intentos)

# Comienza el juego
print("adivina el videojuego (dificil)")
print("(creado por alfonso carrero, en colaboración de andrés otero)")
print("en caso de espacio en el nombre no pongas nada, se reconoce como espacio")

while True:
    mostrar_estado()
    
    # Solicita una suposición al jugador
    suposicion = input("Adivina una letra o la palabra completa: ").lower()
    
    # Verifica si la suposición es una letra o la palabra completa
    if len(suposicion) == 1 and suposicion.isalpha():
        if suposicion in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif suposicion in palabra_objetivo:
            letras_adivinadas.append(suposicion)
        else:
            intentos += 1
    elif suposicion == palabra_objetivo:
        print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
        print("vuelve a jugar cuando quieras :D")
        input()
        
        break
    else:
        print("Suposición no válida.")

    # Verifica si el jugador ha ganado o perdido
    if set(letras_adivinadas) == set(palabra_objetivo):
        mostrar_estado()
        print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
        print("vuelve a jugar cuando quieras :D")
        input()
        break
    elif intentos >= max_intentos:
        mostrar_estado()
        print("¡Has agotado todos los intentos! La palabra correcta era:", palabra_objetivo)
        print("vuelve a jugar cuando quieras :D")
        input()
        break
input()