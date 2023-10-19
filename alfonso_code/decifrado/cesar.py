def descifrar_cesar(ciphertext):
    for shift in range(26):  # Prueba todos los posibles desplazamientos
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                # Comprueba si el carácter es una letra
                is_upper = char.isupper()
                char = char.lower()  # Convierte a minúsculas para el descifrado
                shifted = ord(char) - shift
                if shifted < ord('a'):
                    shifted += 26  # Maneja los desplazamientos fuera del alfabeto
                decrypted_char = chr(shifted)
                if is_upper:
                    decrypted_char = decrypted_char.upper()
                decrypted_text += decrypted_char
            else:
                decrypted_text += char  # Mantén los caracteres no alfabéticos sin cambios
        print(f"Desplazamiento {shift}: {decrypted_text}")

# Solicita una oración del usuario
ciphertext = input("Ingrese la oración cifrada: ")
descifrar_cesar(ciphertext)
input()