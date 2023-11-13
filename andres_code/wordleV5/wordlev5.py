import random
from lista1 import juegos
from lista2 import nombres2
from lista3 import articulos

def seleccionar_biblioteca():
    while True:
        print("Selecciona el modo de juego:")
        print("1. Videojuegos")
        print("2. Clase")
        print("3. Random")
        modo = input("Ingresa el número correspondiente al modo: ")
        
        if modo == '1':
            return juegos
        elif modo == '2':
            return nombres2
        elif modo == '3':
            return articulos
        else:
            print("Modo no válido. Por favor, selecciona 1, 2 o 3.")

# Seleccionar la biblioteca según el modo de juego
biblioteca = seleccionar_biblioteca()

# Elige una palabra aleatoria de la lista
palabra_objetivo = random.choice(biblioteca)

# Resto del código (sin cambios)
intentos = 0
max_intentos = 10
letras_adivinadas = []

def mostrar_estado():
    palabra_mostrada = ""
    for letra in palabra_objetivo:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    print("\nPalabra: " + palabra_mostrada)
    print("Intentos restantes:", max_intentos - intentos)

print("Adivina la palabra (dificil)")
print("(creado por alfonso carrero, en colaboración de andrés otero)")
print("en caso de espacio en el nombre no pongas nada, se reconoce como espacio")

while True:
    mostrar_estado()
    
    suposicion = input("Adivina una letra o la palabra completa: ").lower()
    
    if len(suposicion) == 1 and suposicion.isalpha():
        if suposicion in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif suposicion in palabra_objetivo:
            letras_adivinadas.append(suposicion)
        else:
            intentos += 1
    elif suposicion == palabra_objetivo:
        print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
        print("¡Vuelve a jugar cuando quieras! :D")
        input()
        break
    else:
        print("Suposición no válida.")

    if set(letras_adivinadas) == set(palabra_objetivo):
        mostrar_estado()
        print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
        print("¡Vuelve a jugar cuando quieras! :D")
        input()
        break
    elif intentos >= max_intentos:
        mostrar_estado()
        print("¡Has agotado todos los intentos! La palabra correcta era:", palabra_objetivo)
        print("¡Vuelve a jugar cuando quieras! :D")
        input()
        break
input()

