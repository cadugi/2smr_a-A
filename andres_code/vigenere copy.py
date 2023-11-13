#!/usr/bin/env python
# -*- coding: utf-8 -*-
from claves import clave_adri, clave_david, clave_fonsi
LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
def main():
    mensaje=input("Mensaje: ")
    myKey=input("Clave deseada: (1/2/3)  ")

    if myKey=='1':
        myKey=clave_fonsi
    elif myKey=='2':
        myKey=clave_adri
    elif myKey=='3':
        myKey=clave_david
    else:
        print("Clave no válida")

    accion=input("Mode encriptar o descifrar: (e/d)  ")

    if accion=='e':
        traducido=cifrar_mensaje(myKey,mensaje)
    elif accion=='d':
        traducido=descifrar_mensaje(myKey,mensaje)
    print(traducido)

def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'e')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'d')

def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='e':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='d':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)
if __name__ == '__main__':
    main()
input()