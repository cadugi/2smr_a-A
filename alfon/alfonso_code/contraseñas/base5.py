import string
import random
from cryptography.fernet import Fernet
import os
import csv

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_contrasenas = os.path.join(directorio_actual, "contrasenas.csv")
archivo_clave = os.path.join(directorio_actual, "clave_maestra.key")

# Cargar o generar la clave maestra
if os.path.exists(archivo_clave):
    with open(archivo_clave, "rb") as clave_file:
        clave_maestra = clave_file.read()
else:
    clave_maestra = Fernet.generate_key()
    with open(archivo_clave, "wb") as clave_file:
        clave_file.write(clave_maestra)

fernet = Fernet(clave_maestra)

def generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales):
    caracteres = ""
    if incluir_numeros:
        caracteres += string.digits
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiales:
        caracteres += string.punctuation

    contrasena_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
    contrasena_cifrada = fernet.encrypt(contrasena_generada.encode())
    return contrasena_cifrada

def guardar_contrasena(usuario, contrasena):
    with open(archivo_contrasenas, "a", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([usuario, contrasena.decode()])
    print("Contraseña guardada con éxito.")

def ver_contraseñas():
    try:
        with open(archivo_contrasenas, "r", newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                usuario = fila[0]
                contrasena_cifrada = fila[1]
                contrasena_descifrada = fernet.decrypt(contrasena_cifrada.encode()).decode()
                print(f"Usuario/Correo: {usuario}")
                print(f"Contraseña descifrada: {contrasena_descifrada}")
                print()
    except FileNotFoundError:
        print("No se encontró el archivo de contraseñas.")

def descifrar_contraseña():
    usuario = input("Ingrese el usuario del que desea descifrar la contraseña: ")
    try:
        with open(archivo_contrasenas, "r", newline='') as archivo:
            lector = csv.reader(archivo)
            usuario_encontrado = False
            for fila in lector:
                if fila[0] == usuario:
                    contrasena_cifrada = fila[1]
                    usuario_encontrado = True
                    break
            if usuario_encontrado:
                contrasena_descifrada = fernet.decrypt(contrasena_cifrada.encode()).decode()
                print(f"Contraseña descifrada para {usuario}: {contrasena_descifrada}")
            else:
                print("Usuario no encontrado o contraseña maestra incorrecta.")
    except FileNotFoundError:
        print("No se encontró el archivo de contraseñas.")

while True:
    opcion = input("¿Deseas generar una nueva contraseña (G), ver contraseñas (V), descifrar contraseña (D) o salir (S)? ").strip().lower()

    if opcion == "g":
        usuario = input("Ingrese su usuario/correo: ")
        longitud = int(input("Longitud de la contraseña: "))
        incluir_numeros = input("¿Incluir números? (S/N): ").strip().lower() == "s"
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (S/N): ").strip().lower() == "s"
        incluir_minusculas = input("¿Incluir letras minúsculas? (S/N): ").strip().lower() == "s"
        incluir_especiales = input("¿Incluir caracteres especiales? (S/N): ").strip().lower() == "s"

        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales)
        guardar_contrasena(usuario, contrasena)
    elif opcion == "v":
        ver_contraseñas()
    elif opcion == "d":
        descifrar_contraseña()
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'G' para generar una nueva contraseña, 'V' para ver contraseñas, 'D' para descifrar contraseña o 'S' para salir.")
