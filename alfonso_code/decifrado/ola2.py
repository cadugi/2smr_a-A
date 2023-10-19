def descifrar_oracion(oracion_cifrada):
    resultado = ""
    avanzar = True

    for caracter in oracion_cifrada:
        if caracter.isalpha():
            # Calcular el nuevo valor ASCII
            if avanzar:
                nuevo_ascii = ord(caracter) - 1
            else:
                nuevo_ascii = ord(caracter) + 3

            # Alternar la dirección para el siguiente caracter
            avanzar = not avanzar

            # Asegurarse de que el nuevo valor ASCII esté dentro del rango de letras
            if caracter.islower():
                if nuevo_ascii > ord('z'):
                    nuevo_ascii -= 26
                if nuevo_ascii < ord('a'):
                    nuevo_ascii += 26
            elif caracter.isupper():
                if nuevo_ascii > ord('Z'):
                    nuevo_ascii -= 26
                if nuevo_ascii < ord('A'):
                    nuevo_ascii += 26

            resultado += chr(nuevo_ascii)
        else:
            resultado += caracter

    return resultado

# Solicitar la oración cifrada al usuario
oracion_cifrada = input("Ingresa la oración cifrada que deseas descifrar: ")
oracion_descifrada = descifrar_oracion(oracion_cifrada)
print(f"Oración cifrada: {oracion_cifrada}")
print(f"Oración descifrada: {oracion_descifrada}")
input()