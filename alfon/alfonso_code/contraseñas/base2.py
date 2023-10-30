import os
import string
import random
import pyperclip

def cifrar_cesar(texto, clave):
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_inicial = ord('a') if caracter.islower() else ord('A')
            indice = (ord(caracter) - ascii_inicial + clave) % 26
            texto_cifrado += chr(indice + ascii_inicial)
        elif caracter.isdigit():
            indice = (int(caracter) + clave) % 10
            texto_cifrado += str(indice)
        else:
            texto_cifrado += caracter
    return texto_cifrado

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
    try:
        with open("contrasenas.txt", "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lineas = []

    with open("contrasenas.txt", "w") as archivo:
        usuario_encontrado = False
        for i in range(0, len(lineas), 3):
            usuario_guardado = lineas[i].strip()
            contrasena_guardada = lineas[i + 1].strip()
            if usuario_guardado == f"Usuario/Correo: {usuario}":
                usuario_encontrado = True
                contrasena_cifrada = cifrar_cesar(contrasena, 13)
                archivo.write(f"Usuario/Correo: {usuario}\nContraseña cifrada: {contrasena_cifrada}\n\n")
            else:
                archivo.write(lineas[i])
                archivo.write(lineas[i + 1])
                archivo.write(lineas[i + 2])
        
        if not usuario_encontrado:
            contrasena_cifrada = cifrar_cesar(contrasena, 13)
            archivo.write(f"Usuario/Correo: {usuario}\nContraseña cifrada: {contrasena_cifrada}\n\n")

def ver_contraseñas():
    try:
        with open("contrasenas.txt", "r") as archivo:
            contrasenas = archivo.read()
            print("Contraseñas almacenadas:\n")
            print(contrasenas)
    except FileNotFoundError:
        print("No se encontraron contraseñas almacenadas.")

while True:
    opcion = input("¿Deseas almacenar una contraseña (A), generar una nueva (G), ver contraseñas (V) o salir (S)? ").strip().lower()

    if opcion == "a":
        usuario = input("Ingrese su usuario/correo: ")
        contrasena = input("Ingrese su contraseña: ")
        guardar_contrasena(usuario, contrasena)
        print("Contraseña cifrada y almacenada correctamente en el archivo contrasenas.txt.")
    elif opcion == "g":
        usuario = input("Ingrese su usuario/correo: ")  # Añadido para que el usuario ingrese su nombre de usuario
        longitud = int(input("Longitud de la contraseña: "))
        incluir_numeros = input("¿Incluir números? (S/N): ").strip().lower() == "s"
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (S/N): ").strip().lower() == "s"
        incluir_minusculas = input("¿Incluir letras minúsculas? (S/N): ").strip().lower() == "s"
        incluir_especiales = input("¿Incluir caracteres especiales? (S/N): ").strip().lower() == "s"

        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales)
        guardar_contrasena(usuario, contrasena)
        pyperclip.copy(contrasena)
        print("Contraseña generada y copiada al portapapeles. Además, se ha almacenado en el archivo contrasenas.txt.")
    elif opcion == "v":
        ver_contraseñas()
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'A' para almacenar una contraseña, 'G' para generar una nueva, 'V' para ver contraseñas, o 'S' para salir.")
