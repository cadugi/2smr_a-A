# Valores proporcionados
M = int(input("Ingresa el mensaje a cifrar (M): "))
k = int(input("Ingresa el número coprimo (k): "))
n = int(input("Ingresa el valor de n (p*q): "))

# Cifrado
C = (M ** k) % n

print(f"Mensaje cifrado (C): {C}")
