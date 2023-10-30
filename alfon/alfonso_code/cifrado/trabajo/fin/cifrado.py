# Datos proporcionados por el mensajero
M = 4237  # Mensaje a cifrar

# Clave pública del mensajero
e = 13127  # Exponente de cifrado
n = 29435020  # Módulo (p * q)

# Cifrado del mensaje
C = (M**e) % n

print(f"Mensaje cifrado (C): {C}")
