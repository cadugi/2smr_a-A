import random
from lista1 import juegos
from lista2 import nombres2
from lista3 import articulos
from colorama import init, Fore
from IPython.display import clear_output

init(autoreset=True)

dibujos_ahorcado = [
    """
     _____
    |     |
          |
          |
          |
          |
    """,
    """
     _____
    |     |
    O     |
          |
          |
          |
    """,
    """
     _____
    |     |
    O     |
    |     |
          |
          |
    """,
    """
     _____
    |     |
    O     |
   /|     |
          |
          |
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
          |
          |
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   /      |
          |
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   / \\    |
          |
    """
]

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

def seleccionar_dificultad():
    while True:
        print("Selecciona la dificultad:")
        print(f"{Fore.GREEN}1. Fácil (6 intentos){Fore.RESET}")
        print(f"{Fore.YELLOW}2. Normal (5 intentos){Fore.RESET}")
        print(f"{Fore.MAGENTA}3. Difícil (3 intentos){Fore.RESET}")
        print(f"{Fore.RED}4. Extremo (1 intento){Fore.RESET}")
        dificultad = input("Ingresa el número correspondiente a la dificultad: ")
        
        if dificultad == '1':
            return 6
        elif dificultad == '2':
            return 5
        elif dificultad == '3':
            return 3
        elif dificultad == '4':
            return 1
        else:
            print("Dificultad no válida. Por favor, selecciona 1, 2, 3 o 4.")

def jugar():
    while True:
        continuar_jugando = True  # Variable para controlar si el jugador desea continuar jugando

        while continuar_jugando:  # Bucle principal para continuar jugando
            biblioteca = seleccionar_biblioteca()
            dificultad = seleccionar_dificultad()

            palabra_objetivo = random.choice(biblioteca)

            intentos = 0
            max_intentos = dificultad
            letras_adivinadas = []
            letras_incorrectas = []

            def mostrar_estado():
                clear_output()  # Borra la salida anterior
                palabra_mostrada = ""
                palabra_completa = True  # Variable para rastrear si se ha adivinado la palabra completa
                for letra in palabra_objetivo:
                    if letra == "_":
                        palabra_mostrada += " "  # Espacio en blanco
                    elif letra in letras_adivinadas:
                        palabra_mostrada += Fore.GREEN + letra + " " + Fore.RESET
                    else:
                        palabra_mostrada += "_ "
                        palabra_completa = False  # Si falta alguna letra, la palabra no está completa
                print("\nPalabra: " + palabra_mostrada)
                
                # Si palabra_completa sigue siendo True, significa que todas las letras han sido adivinadas
                if palabra_completa:
                    print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
                    return True  # Indica que el juego se ha ganado

                print("Intentos restantes:", max_intentos - intentos)
                print(dibujos_ahorcado[intentos])
                print(Fore.RED + "Letras incorrectas:", ", ".join(letras_incorrectas) + Fore.RESET)

            print("Adivina la palabra (dificultad)")
            print("(creado por Cadugi, en colaboración de Hôdr)")
            print("en caso de espacio en el nombre no pongas nada, se reconoce como espacio")

            while True:
                if mostrar_estado():  # Si mostrar_estado retorna True, el juego se ganó
                    break

                suposicion = input("Adivina una letra o la palabra completa: ").lower()
                
                if len(suposicion) == 1 and (suposicion.isalpha() or suposicion == '_' or suposicion.isdigit()):
                    if suposicion in letras_adivinadas:
                        print("Ya has adivinado esa letra.")
                    elif suposicion in palabra_objetivo:
                        letras_adivinadas.append(suposicion)
                    else:
                        intentos += 1
                        letras_incorrectas.append(suposicion)
                elif suposicion == palabra_objetivo:
                    print("¡Felicidades! Has adivinado la palabra correcta:", palabra_objetivo)
                    break  #
                else:
                    print("Suposición no válida.")
                    
                if intentos >= max_intentos:
                    print("¡Has agotado todos los intentos! La palabra correcta era:", palabra_objetivo)
                    break

            reiniciar = input("¿Quieres jugar de nuevo? (s/n): ")
            if reiniciar.lower() != 's':
                continuar_jugando = False  # Terminar el juego si el jugador no quiere jugar de nuevo

if __name__ == "__main__":
    jugar()
