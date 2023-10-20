from string import ascii_lowercase, ascii_uppercase, digits

def cifrado(texto, pasos):
    resultado = []

    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevo_indice])
        elif c in digits:
            indice = digits.index(c)
            nuevo_indice = (indice + pasos) % len(digits)
            resultado.append(digits[nuevo_indice])
    return ''.join(resultado)


texto = '123Este texto va ha ser gracioso789'
print(cifrado(texto, 15))
input()