import pyautogui
import time
from spamlibra import letra2

time.sleep(5)

i = 0
while i < len(letra2):
    pyautogui.write(letra2[i])
    pyautogui.press('enter')  # Presiona enter para enviar la línea
    time.sleep(1)  # Espera 5 segundos antes de la próxima línea
    i += 1