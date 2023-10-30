from sympy import Pow

# Datos proporcionados por el receptor
C = 19286710  # Mensaje cifrado
j = 3434143219.7136436  # Clave privada
n = 29435020  # Módulo (p * q)

# Descifrado del mensaje
M = Pow(C, j, n)

print(f"Mensaje descifrado (M): {M}")
input()