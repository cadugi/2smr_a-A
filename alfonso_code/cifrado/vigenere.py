def cifrado_vigenere(texto, clave):
    resultado = ""
    clave_repetida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            nueva_letra = chr(((ord(texto[i]) + ord(clave_repetida[i]) - 2 * 65) % 26) + 65)
            resultado += nueva_letra
        else:
            resultado += texto[i]
    return resultado

texto_original = "Hola, mundo!"
clave = "PYTHON"
texto_cifrado = cifrado_vigenere(texto_original.upper(), clave.upper())
print(texto_cifrado)
