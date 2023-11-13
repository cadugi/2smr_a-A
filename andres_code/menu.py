from fractions import Fraction

# Función para cifrar el mensaje
def cifrar_mensaje():
    try:
        M = int(input("Ingresa el mensaje a cifrar (M, del emisor): "))
        k = Fraction(input("Ingresa el valor de k (del emisor): "))
        n = int(input("Ingresa el valor de n (del receptor): "))
        C = pow(M, k.numerator, n)
        print(f"Mensaje cifrado (C): {C}")
    except ValueError:
        print("Error: Ingresa un valor numérico válido para M, k y n.")

# Función para descifrar el mensaje
def descifrar_mensaje():
    try:
        C = int(input("Ingresa el mensaje cifrado (C, del receptor): "))
        j = Fraction(input("Ingresa el valor de j (del receptor): "))
        n = int(input("Ingresa el valor de n (del receptor): "))
        
        if j.denominator != 1:  # Verifica que j sea un número entero
            print("Error: j debe ser un número entero.")
            return

        j = j.numerator  # Obtiene el numerador de j
        M = pow(C, j, n)
        print(f"Mensaje descifrado (M): {M}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos para C, j y n.")

# Función para calcular la clave privada j de manera iterativa
def calcular_clave_privada():
    x = Fraction(input("Ingresa el valor de x (del receptor): "))
    z = Fraction(input("Ingresa el valor de z (del receptor): "))
    k = Fraction(input("Ingresa el valor de k (del receptor): "))

    j = None
    while j is None or j.denominator != 1:
        x += 1
        j = (1 + x * z) / k

    j = j.numerator  # Obtiene el numerador de j (número entero)
    print(f"Clave privada (j): {j}")

while True:
    print("\nSelecciona una opción:")
    print("1. Cifrar mensaje (emisor)")
    print("2. Descifrar mensaje (receptor)")
    print("3. Calcular clave privada (receptor)")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == '1':
        cifrar_mensaje()
    elif opcion == '2':
        descifrar_mensaje()
    elif opcion == '3':
        calcular_clave_privada()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
input()