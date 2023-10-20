from cryptography.fernet import Fernet

# Genera una clave aleatoria para AES-256
def generar_clave():
    return Fernet.generate_key()

# Cifra datos con AES-256
def cifrar(datos, clave):
    f = Fernet(clave)
    datos_cifrados = f.encrypt(datos.encode())
    return datos_cifrados

# Descifra datos con AES-256
def descifrar(datos_cifrados, clave):
    f = Fernet(clave)
    datos_descifrados = f.decrypt(datos_cifrados).decode()
    return datos_descifrados

# Ejemplo de uso
if __name__ == "__main__":
    clave = generar_clave()
    datos_a_cifrar = "Alfonso, te paso el bocadillo?"

    datos_cifrados = cifrar(datos_a_cifrar, clave)
    print(f"Datos cifrados: {datos_cifrados}")

    datos_descifrados = descifrar(datos_cifrados, clave)
    print(f"Datos descifrados: {datos_descifrados}")
print (clave)    
input()