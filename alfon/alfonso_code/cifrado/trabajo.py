import math

def encontrar_entero(z, k):
    x = 0
    while True:
        x += 1
        resultado = (1 + x * z) / k
        if math.isclose(resultado, round(resultado)):
            return round(resultado)

z = float(input("Ingrese el valor de z: "))
k = float(input("Ingrese el valor de k: "))

resultado_entero = encontrar_entero(z, k)
print("El primer número entero sin decimales es:", resultado_entero)
input()