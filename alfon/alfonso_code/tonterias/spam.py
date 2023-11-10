import pyautogui
import time

# Letra de la canción
letra = [

"We're no strangers to love"
"You know the rules and so do I (do I)"
"A full commitment's what I'm thinking of"
"You wouldn't get this from any other guy"
"I just wanna tell you how I'm feeling"
"Gotta make you understand"
"Never gonna give you up"
"Never gonna let you down"
"Never gonna run around and desert you"
"Never gonna make you cry"
"Never gonna say goodbye"
"Never gonna tell a lie and hurt you"
"We've known each other for so long"
"Your heart's been aching, but you're too shy to say it (to say it)"
"Inside, we both know what's been going on (going on)"
"We know the game and we're gonna play it"
"And if you ask me how I'm feeling"
]

# Escribe cada línea con un retraso de 5 segundos
for linea in letra:
    pyautogui.write(linea)
    pyautogui.press('enter')  # Presiona enter para enviar la línea
    time.sleep(5)  # Espera 5 segundos antes de la próxima línea
