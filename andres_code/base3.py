import os
import string
import random
from cryptography.fernet import Fernet

# Genera una clave para cifrar/descifrar contraseñas (debes mantener esta clave de manera segura)
clave_maestra = Fernet.generate_key()
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
    with open("contrasenas.txt", "ab") as archivo:  # Modifica "ab" para modo binario
        archivo.write(f"Usuario/Correo: {usuario}\nContraseña cifrada: {contrasena}\n\n".encode())

def ver_contraseñas():
    try:
        with open("contrasenas.txt", "rb") as archivo:  # Modifica "rb" para modo binario
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 3):
                usuario = lineas[i].strip().split(b" ")[1]
                contrasena_cifrada = lineas[i + 1].strip().split(b" ")[2]
                print(f"Usuario/Correo: {usuario.decode()}")
                print(f"Contraseña cifrada: {contrasena_cifrada.decode()}")
                print()
    except FileNotFoundError:
        print("No se encontraron contraseñas almacenadas.")

def descifrar_contraseña():
    usuario = input("Ingrese el usuario del que desea descifrar la contraseña: ")
    contrasena_cifrada = None
    with open("contrasenas.txt", "rb") as archivo:
        lineas = archivo.readlines()
        for i in range(0, len(lineas), 3):
            usuario_guardado = lineas[i].strip().split(b" ")[1]
            if usuario == usuario_guardado.decode():
                contrasena_cifrada = lineas[i + 1].strip().split(b" ")[2]
                break

    if contrasena_cifrada:
        contrasena_descifrada = fernet.decrypt(contrasena_cifrada).decode()
        print(f"Contraseña descifrada para {usuario}: {contrasena_descifrada}")
    else:
        print("Usuario no encontrado o contraseña maestra incorrecta.")

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
        print("Contraseña generada y almacenada en el archivo contrasenas.txt.")
    elif opcion == "v":
        ver_contraseñas()
    elif opcion == "d":
        descifrar_contraseña()
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'G' para generar una nueva contraseña, 'V' para ver contraseñas, 'D' para descifrar contraseña o 'S' para salir.")
input()