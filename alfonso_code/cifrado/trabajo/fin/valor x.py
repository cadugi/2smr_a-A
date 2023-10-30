import math

def encontrar_entero(z, k, x_inicial):
    x = x_inicial
    while True:
        x += 1
        resultado = (1 + x * z) / k
        if math.isclose(resultado, round(resultado)):
            return round(resultado)

z = float(input("Ingrese el valor de z: "))
k = float(input("Ingrese el valor de k: "))

x_inicial = 0
resultado_entero = encontrar_entero(z, k, x_inicial)

while True:
    print("El primer número entero sin decimales es:", resultado_entero)

    respuesta = input("¿Quieres buscar el siguiente entero? (s/n): ")
    if respuesta.lower() != "s":
        break

    x_inicial = resultado_entero + 1
    resultado_entero = encontrar_entero(z, k, x_inicial)
input()