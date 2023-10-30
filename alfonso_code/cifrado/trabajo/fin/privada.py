# Solicitar los valores de x, z y k al usuario
x = int(input("Ingresa el valor de x: "))
z = int(input("Ingresa el valor de z: "))
k = int(input("Ingresa el valor de k: "))

# Calcular la clave privada j
j = (1 + x * z) / k

# Imprimir la clave privada j
print(f"Clave privada (j): {j}")
input()