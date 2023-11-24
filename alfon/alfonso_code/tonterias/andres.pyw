import ctypes
import time
import webbrowser
import pyautogui
import subprocess


def mostrar_mensaje_emergente():
    ctypes.windll.user32.MessageBoxW(0, "Andres, estas jodido macho", "Mensaje de Andres", 1)

    # Espera 1 segundo antes de abrir el navegador
    time.sleep(1)
    
    abrir_navegador()

def abrir_navegador():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)

    # Espera 3 segundos antes de enviar la tecla F
    time.sleep(3)
    

    # Espera 15 segundos antes de mostrar la pregunta
    time.sleep(15)
    
    preguntar_guardado()

def preguntar_guardado():
    ctypes.windll.user32.MessageBoxW(0, "¿Tienes todo guardado? hazlo antes de tocar nada ya que puedes perderlo", "Pregunta", 1)

    # Mostrar un mensaje de despedida sin opción de respuesta
    ctypes.windll.user32.MessageBoxW(0, "Bye bye", "Mensaje de Despedida", 0x40)  # 0x40 es el código de MB_ICONINFORMATION
    
    # Iniciar la cuenta regresiva desde 5 hasta 0
    contar_regresiva()

def contar_regresiva():
    for i in range(5, 0, -1):
        time.sleep(1)
        ctypes.windll.user32.MessageBoxW(0, str(i), "Cuenta Regresiva", 0x40)  # 0x40 es el código de MB_ICONINFORMATION

    # Mostrar el último mensaje "0"
    ctypes.windll.user32.MessageBoxW(0, "0", "Cuenta Regresiva", 0x40)

    # Apagar el equipo después de la cuenta regresiva
    apagar_equipo()

def apagar_equipo():
    subprocess.run(["shutdown", "/s", "/t", "1"])

# Llamamos a la función principal
mostrar_mensaje_emergente()
