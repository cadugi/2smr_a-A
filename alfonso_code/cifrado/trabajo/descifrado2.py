# Valores proporcionados
C = int(input("Ingresa el mensaje cifrado (C): "))
j = int(input("Ingresa otro número coprimo (j): "))
n = int(input("Ingresa el valor de n (p*q): "))

# Descifrado
M = (C ** j) % n

print(f"Mensaje descifrado (M): {M}")
