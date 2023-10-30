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
    contrasenas = leer_contrasenas()
    usuario_existente = False
    for i, (u, _) in enumerate(contrasenas):
        if u == usuario:
            contrasenas[i] = (usuario, contrasena.decode())
            usuario_existente = True
            break
    if not usuario_existente:
        contrasenas.append((usuario, contrasena.decode()))

    escribir_contrasenas(contrasenas)
    print("Contraseña guardada con éxito.")

def leer_contrasenas():
    contrasenas = []
    try:
        with open(archivo_contrasenas, "r", newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                usuario = fila[0]
                contrasena_cifrada = fila[1]
                contrasenas.append((usuario, contrasena_cifrada))
        return contrasenas
    except FileNotFoundError:
        return []

def escribir_contrasenas(contrasenas):
    with open(archivo_contrasenas, "w", newline='') as archivo:
        escritor = csv.writer(archivo)
        for usuario, contrasena_cifrada in contrasenas:
            escritor.writerow([usuario, contrasena_cifrada])

def ver_contraseñas():
    contrasenas = leer_contrasenas()
    if not contrasenas:
        print("No se encontraron contraseñas almacenadas.")
    else:
        for usuario, contrasena_cifrada in contrasenas:
            contrasena_descifrada = fernet.decrypt(contrasena_cifrada.encode()).decode()
            print(f"Usuario/Correo: {usuario}")
            print(f"Contraseña descifrada: {contrasena_descifrada}")
            print()

def cifrar_archivo_csv():
    contrasenas = leer_contrasenas()
    contrasenas_cifradas = []
    for usuario, contrasena in contrasenas:
        contrasena_cifrada = fernet.encrypt(contrasena.encode())
        contrasenas_cifradas.append((usuario, contrasena_cifrada.decode()))
    
    with open(archivo_contrasenas, "w", newline='') as archivo:
        escritor = csv.writer(archivo)
        for usuario, contrasena_cifrada in contrasenas_cifradas:
            escritor.writerow([usuario, contrasena_cifrada])
    print("Archivo .csv cifrado con éxito.")

def descifrar_archivo_csv():
    contrasenas_cifradas = leer_contrasenas()
    contrasenas_descifradas = []
    for usuario, contrasena_cifrada in contrasenas_cifradas:
        contrasena = fernet.decrypt(contrasena_cifrada.encode()).decode()
        contrasenas_descifradas.append((usuario, contrasena))
    
    with open(archivo_contrasenas, "w", newline='') as archivo:
        escritor = csv.writer(archivo)
        for usuario, contrasena in contrasenas_descifradas:
            escritor.writerow([usuario, contrasena])
    print("Archivo .csv descifrado con éxito.")

while True:
    opcion = input("¿Deseas generar una nueva contraseña (G), ver contraseñas (V), cifrar archivo (C), descifrar archivo (D) o salir (S)? ").strip().lower()

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
    elif opcion == "c":
        cifrar_archivo_csv()
    elif opcion == "d":
        descifrar_archivo_csv()
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'G' para generar una nueva contraseña, 'V' para ver contraseñas, 'C' para cifrar archivo, 'D' para descifrar archivo o 'S' para salir.")
