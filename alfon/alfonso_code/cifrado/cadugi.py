def encriptar_oracion(oracion):
    oracion_encriptada = ""
    
    for caracter in oracion:
        if caracter.isalpha():
            # Aplicamos la primera parte del encriptado (salto de letras)
            caracter_encriptado = chr(ord(caracter) + 2)
            
            # Si el caracter encriptado supera 'z' o 'Z', restamos 26 para volver al inicio del alfabeto
            if caracter.islower() and ord(caracter_encriptado) > ord('z'):
                caracter_encriptado = chr(ord(caracter_encriptado) - 26)
            elif caracter.isupper() and ord(caracter_encriptado) > ord('Z'):
                caracter_encriptado = chr(ord(caracter_encriptado) - 26)
            
            # Aplicamos la segunda parte del encriptado (desplazamiento a la derecha)
            caracter_encriptado = chr(ord(caracter_encriptado) + 1)
            
            # Si el caracter encriptado supera 'z' o 'Z' nuevamente, restamos 26 para volver al inicio del alfabeto
            if caracter.islower() and ord(caracter_encriptado) > ord('z'):
                caracter_encriptado = chr(ord(caracter_encriptado) - 26)
            elif caracter.isupper() and ord(caracter_encriptado) > ord('Z'):
                caracter_encriptado = chr(ord(caracter_encriptado) - 26)
        else:
            # Si no es un carácter alfabético, simplemente lo agregamos sin encriptar
            caracter_encriptado = caracter
        
        oracion_encriptada += caracter_encriptado
    
    return oracion_encriptada

# Solicitar al usuario que ingrese la oración
oracion = input("Ingresa una oración: ")
oracion_encriptada = encriptar_oracion(oracion)
print("Oración encriptada:", oracion_encriptada)
input()