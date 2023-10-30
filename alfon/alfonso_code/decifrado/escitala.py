def descifrar_escitala(cifrado, num_filas):
    longitud_cifrado = len(cifrado)
    longitud_columnas = longitud_cifrado // num_filas
    if longitud_cifrado % num_filas != 0:
        longitud_columnas += 1

    descifrado = [[' ' for _ in range(longitud_columnas)] for _ in range(num_filas)]

    fila, columna = 0, 0
    for letra in cifrado:
        if letra == 'k':
            letra = ' '  # Reemplazar 'k' por un espacio
        descifrado[fila][columna] = letra
        fila += 1
        if fila == num_filas:
            fila = 0
            columna += 1

    mensaje_descifrado = ''
    for fila in range(num_filas):
        for columna in range(longitud_columnas):
            mensaje_descifrado += descifrado[fila][columna]

    return mensaje_descifrado


def main():
    cifrado = input("Introduce la oración encriptada: ")
    for num_filas in range(2, len(cifrado)):
        descifrado = descifrar_escitala(cifrado, num_filas)
        print(f"Combinación con {num_filas} filas:")
        print(descifrado)
        print()


if __name__ == "__main__":
    main()
    input()
