import pyperclip

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            nueva_letra = chr(((ord(letra) - 65 + desplazamiento) % 26) + 65)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

while True:
    contrasena = input("Ingrese la contraseña: ")

    if contrasena == "4237":
        desplazamiento = 257
    else:
        desplazamiento = 3  # Valor predeterminado si la contraseña es incorrecta.

    texto_original = input("Ingrese la palabra a codificar: ")

    texto_cifrado = cifrado_cesar(texto_original.upper(), desplazamiento)
    
    mostrar_cifrado = input("¿Mostrar texto cifrado? (A para mostrar, cualquier otra tecla para continuar): ")
    if mostrar_cifrado.upper() == "A":
        print("Texto cifrado:", texto_cifrado)
        
    copiar = input("¿Desea copiar el texto cifrado al portapapeles? (C para copiar, cualquier otra tecla para continuar): ")
    if copiar.upper() == "C":
        pyperclip.copy(texto_cifrado)
        print("Texto cifrado copiado al portapapeles.")

    mensaje_nuevamente = """¿Desea codificar otra palabra?
    (Y para sí, N para no): """
    nuevamente = input(mensaje_nuevamente)
    if nuevamente.upper() != "Y":
        break
