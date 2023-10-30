from fractions import Fraction

def calcular_clave_privada():
    x = Fraction(input("Ingresa el valor de x: "))
    z = Fraction(input("Ingresa el valor de z: "))
    k = Fraction(input("Ingresa el valor de k: "))

    j = None
    while j is None or j.denominator != 1:
        x += 1
        j = (1 + x * z) / k

    j = j.numerator  # Obtiene el numerador de j (número entero)
    print(f"Clave privada (j): {j}")

calcular_clave_privada()
input()