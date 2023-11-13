import random
from colorama import init, Fore
from IPython.display import clear_output
import time

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

def obtener_intentos_truco():
    trucos = ["trucos"]  # Palabras clave para activar el truco
    suposicion = input("Escribe 'trucos' para obtener 99 intentos secretos: ").lower()
    return suposicion in trucos

def seleccionar_biblioteca():
    while True:
        print("Selecciona el modo de juego:")
        print("1. Videojuegos")
        print("2. Clase")
        print("3. Random")
        modo = input("Ingresa el número correspondiente al modo: ")

        print("Cargando...")
        time.sleep(1.5)

        if modo == '1':
            from lista1 import juegos
            return juegos
        elif modo == '2':
            from lista2 import nombres2
            return nombres2
        elif modo == '3':
            from lista3 import articulos
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

        print("Cargando...")
        time.sleep(0.7)

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

def mostrar_estado(palabra_objetivo, letras_adivinadas, letras_incorrectas, intentos, max_intentos):
    clear_output()
    palabra_mostrada = ""
    palabra_completa = True

    for letra in palabra_objetivo:
        if letra == "_":
            palabra_mostrada += " "
        elif letra in letras_adivinadas:
            palabra_mostrada += Fore.GREEN + letra + " " + Fore.RESET
        else:
            palabra_mostrada += "_ "
            palabra_completa = False

    print("\nPalabra: " + palabra_mostrada)

    if palabra_completa:
        print(f"¡Felicidades! Has adivinado la palabra correcta: {palabra_objetivo}")
        return True

    print(f"Intentos restantes: {max_intentos - intentos}")
    print(dibujos_ahorcado[intentos])
    print(Fore.RED + f"Letras incorrectas: {', '.join(letras_incorrectas)}" + Fore.RESET)

    if intentos >= max_intentos:
        print(f"¡Has agotado todos los intentos! La palabra correcta era: {palabra_objetivo}")
        return True

def jugar():
    while True:
        continuar_jugando = True

        while continuar_jugando:
            biblioteca = seleccionar_biblioteca()
            dificultad = seleccionar_dificultad()

            palabra_objetivo = random.choice(biblioteca)

            intentos = 0
            max_intentos = dificultad

            letras_adivinadas = []
            letras_incorrectas = []

            print("Adivina la palabra (dificultad)")
            print("(creado por Cadugi, en colaboración de Hôdr)")
            print("en caso de espacio en el nombre no pongas nada, al intentar adivinar la palabra pon _")

            trucos_activados = False

            while True:
                if mostrar_estado(palabra_objetivo, letras_adivinadas, letras_incorrectas, intentos, max_intentos):
                    break

                if not trucos_activados:
                    suposicion = input("Adivina una letra o la palabra completa: ").lower()
                else:
                    suposicion = input("Adivina una letra o la palabra completa (99 intentos secretos activados): ").lower()

                if suposicion == "trucos":
                    if not trucos_activados:
                        print("¡Trucos activados! Ahora tienes 99 intentos secretos.")
                        trucos_activados = True
                        max_intentos = 99  # Desactiva el límite de intentos
                elif len(suposicion) == 1 and (suposicion.isalpha() or suposicion == '_' or suposicion.isdigit()):
                    if suposicion in letras_adivinadas:
                        print("Ya has adivinado esa letra.")
                    elif suposicion in palabra_objetivo:
                        letras_adivinadas.append(suposicion)
                    else:
                        intentos += 1
                        letras_incorrectas.append(suposicion)
                elif suposicion == palabra_objetivo:
                    print(f"¡Felicidades! Has adivinado la palabra correcta: {palabra_objetivo}")
                    break
                else:
                    print("Suposición no válida.")

                if intentos >= max_intentos:
                    print(f"¡Has agotado todos los intentos! La palabra correcta era: {palabra_objetivo}")
                    break

            reiniciar = input("¿Quieres jugar de nuevo? (s/n): ")
            if reiniciar.lower() != 's':
                continuar_jugando = False

if __name__ == "__main__":
    jugar()

