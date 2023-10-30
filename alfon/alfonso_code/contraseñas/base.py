import os

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

usuario = input("Ingrese su usuario/correo: ")
contrasena = input("Ingrese su contraseña: ")

contrasena_cifrada = cifrar_cesar(contrasena, 13)

archivo = open("contrasenas.txt", "a")
archivo.write(f"Usuario/Correo: {usuario}\nContraseña cifrada: {contrasena_cifrada}\n")
archivo.close()

print("Contraseña cifrada y almacenada correctamente en el archivo contrasenas.txt.")