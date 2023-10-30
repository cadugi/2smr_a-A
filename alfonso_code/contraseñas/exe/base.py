import string
import random
from cryptography.fernet import Fernet
import os
import pickle
import subprocess

# Comando para instalar la biblioteca cryptography
comando_instalacion = "pip install cryptography"

# Intentar instalar cryptography
try:
    subprocess.run(comando_instalacion, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error al instalar cryptography:", e)
    exit(1)

# Importar la biblioteca cryptography después de la instalación
from cryptography.fernet import Fernet

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_contrasenas_bin = os.path.join(directorio_actual, "contrasenas.bin")
archivo_contrasenas_cifrado = os.path.join(directorio_actual, "contrasenas_cifrado.bin")
archivo_clave = os.path.join(directorio_actual, "clave_maestra.key")

# Contraseña maestra predeterminada
contrasena_maestra_predeterminada = "4237alfonso"
contrasena_descifrado = contrasena_maestra_predeterminada

# Crear un objeto Fernet con una clave generada o almacenada previamente
if os.path.exists(archivo_clave):
    with open(archivo_clave, "rb") as clave_file:
        clave_maestra = clave_file.read()
        fernet = Fernet(clave_maestra)
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
            contrasenas[i] = (usuario, contrasena)
            usuario_existente = True
            break
    if not usuario_existente:
        contrasenas.append((usuario, contrasena))

    escribir_contrasenas(contrasenas)
    print("Contraseña guardada con éxito.")

def leer_contrasenas():
    try:
        with open(archivo_contrasenas_cifrado, "rb") as archivo:
            contrasenas_cifradas = archivo.read()
            contrasenas = pickle.loads(fernet.decrypt(contrasenas_cifradas))
        return contrasenas
    except (FileNotFoundError, EOFError):
        return []

def escribir_contrasenas(contrasenas):
    contrasenas_cifradas = fernet.encrypt(pickle.dumps(contrasenas))
    with open(archivo_contrasenas_cifrado, "wb") as archivo:
        archivo.write(contrasenas_cifradas)

def descifrar_contraseña():
    contrasena_ingresada = input("Ingrese la contraseña maestra: ")
    if contrasena_ingresada == contrasena_descifrado:
        contrasenas = leer_contrasenas()
        if not contrasenas:
            print("No se encontraron contraseñas almacenadas.")
        else:
            for usuario, contrasena in contrasenas:
                print(f"Usuario/Correo: {usuario}")
                contrasena_descifrada = fernet.decrypt(contrasena).decode()
                print(f"Contraseña descifrada: {contrasena_descifrada}")
                print()
    else:
        print("Contraseña incorrecta. No se puede descifrar el archivo.")

def cambiar_contraseña_maestra():
    contrasena_actual = input("Introduce la contraseña maestra actual: ")
    if contrasena_actual == contrasena_maestra_predeterminada:
        nueva_contraseña = input("Introduce la nueva contraseña maestra: ")
        # Actualizar la contraseña maestra y la clave Fernet
        with open(archivo_clave, "wb") as clave_file:
            nueva_clave_maestra = Fernet.generate_key()
            clave_file.write(nueva_clave_maestra)
        nueva_fernet = Fernet(nueva_clave_maestra)
        contrasenas = leer_contrasenas()
        for i in range(len(contrasenas)):
            _, contrasena_cifrada = contrasenas[i]
            contrasena = nueva_fernet.decrypt(contrasena_cifrada).decode()
            contrasenas[i] = ("", nueva_fernet.encrypt(contrasena.encode()))
        escribir_contrasenas(contrasenas)
        print("Contraseña maestra cambiada con éxito.")
    else:
        print("Contraseña maestra incorrecta. No se puede cambiar la contraseña.")

while True:
    opcion = input("¿Deseas generar una nueva contraseña (G), descifrar contraseñas (D), cambiar contraseña maestra (C), ver créditos (V) o salir (S)? ").strip().lower()

    if opcion == "g":
        usuario = input("Ingrese su usuario/correo: ")
        longitud = int(input("Longitud de la contraseña: "))
        incluir_numeros = input("¿Incluir números? (S/N): ").strip().lower() == "s"
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (S/N): ").strip().lower() == "s"
        incluir_minusculas = input("¿Incluir letras minúsculas? (S/N): ").strip().lower() == "s"
        incluir_especiales = input("¿Incluir caracteres especiales? (S/N): ").strip().lower() == "s"

        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_mayusculas, incluir_minusculas, incluir_especiales)
        guardar_contrasena(usuario, contrasena)
    elif opcion == "d":
        descifrar_contraseña()
    elif opcion == "c":
        cambiar_contraseña_maestra()
    elif opcion == "v":
        print("Créditos: Alfonso Carrero junto con ChatGPT y la idea de Andrés Otero han creado este programa.")
    elif opcion == "s":
        break
    else:
        print("Opción no válida. Debes elegir 'G' para generar una nueva contraseña, 'D' para descifrar contraseñas, 'C' para cambiar la contraseña maestra, 'V' para ver créditos o 'S' para salir.")
