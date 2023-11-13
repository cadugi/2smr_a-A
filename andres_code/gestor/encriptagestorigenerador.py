import os
import random
import string

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
    return contrasena_generada

def guardar_contrasena(usuario, contrasena):
    with open("contrasenas.txt", "a") as archivo:
        archivo.write(f"Usuario/Correo: {usuario}\nContraseña: {contrasena}\n\n")

def ver_contraseñas():
    try:
        with open("contrasenas.txt", "r") as archivo:
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 3):
                usuario = lineas[i].strip().split(" ")[1]
                contrasena = lineas[i + 1].strip().split(" ")[1]
                print(f"Usuario/Correo: {usuario}")
                print(f"Contraseña: {contrasena}")
                print()
    except FileNotFoundError:
        print("No se encontraron contraseñas almacenadas.")

while True:
    opcion = input("¿Deseas generar una nueva contraseña (G), ver contraseñas (V) o salir (S)? ").strip().lower()

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
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'G' para generar una nueva contraseña, 'V' para ver contraseñas o 'S' para salir.")
input()