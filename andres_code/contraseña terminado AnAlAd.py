
import random
import string
#import pyperclip

respuestalongitud = input("Cuanto quieres que mida?  ")
respuestaletras = input("Quieres letras en tu contraseña? (s/n)   ")
respuestanumeros = input("Quieres numeros en tu contraseña? (s/n)  ")
respuestasimbolos = input("Quieres simbolos o caracteres especiales en tu contraseña? (s/n)  ")
respuestaespacios = input("Quieres espacios en balnco en tu contraseña? (s/n)  ")

def generar_contrasena(longitud, incluir_letras, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_letras:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

longitud = int(respuestalongitud)
incluir_letras = respuestaletras
incluir_numeros = respuestanumeros
incluir_simbolos = respuestasimbolos

if respuestaletras == "s":
    incluir_letras = True
else: 
    incluir_letras = False

if respuestanumeros == "s":
    incluir_numeros = True
else: 
    incluir_numeros = False

if respuestasimbolos == "s":
    incluir_simbolos = True
else: 
    incluir_simbolos = False

contraseña = generar_contrasena(longitud, incluir_letras, incluir_numeros, incluir_simbolos)

print(generar_contrasena(longitud, incluir_letras, incluir_numeros, incluir_simbolos))
#pyperclip.copy(contraseña)
repetir = input("quieres crear otra contraseña? (s/n)  ")
if repetir == "s":
    print(generar_contrasena(longitud, incluir_letras, incluir_numeros, incluir_simbolos))
    repetir = input("quieres crear otra contraseña? (s/n)  ")
else: ""    
input()