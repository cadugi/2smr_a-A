def cesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                plaintext += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            plaintext += char
    return plaintext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.islower():
                shift = ord(key[i % key_length]) - 97
                plaintext += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                shift = ord(key[i % key_length]) - 65
                plaintext += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            plaintext += char
    return plaintext

def substitution_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += key[ord(char) - 97].lower()
            else:
                plaintext += key[ord(char) - 65].upper()
        else:
            plaintext += char
    return plaintext

cipher_text = input("Introduce el texto cifrado: ")
choice = input("Elige el método de descifrado (1 para César, 2 para Vigenère, 3 para Sustitución): ")

if choice == "1":
    shift = int(input("Introduce el valor del desplazamiento (entero): "))
    decrypted_text = cesar_decrypt(cipher_text, shift)
    print("Texto descifrado (César):", decrypted_text)
elif choice == "2":
    key = input("Introduce la clave Vigenère: ")
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print("Texto descifrado (Vigenère):", decrypted_text)
elif choice == "3":
    key = input("Introduce el alfabeto de sustitución: ")
    decrypted_text = substitution_decrypt(cipher_text, key)
    print("Texto descifrado (Sustitución):", decrypted_text)
else:
    print("Método de descifrado no válido.")
input()