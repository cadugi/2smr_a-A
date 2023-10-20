preguntas = ("1.x?: ",
             "2.x?: ",
             "3.x?: ",
             "4.x?: ",
             "5.x?: ")
opciones = (("A.x" , "B.x" , "C.x" , "D.x"),
            ("A.x" , "B.x" , "C.x" , "D.x"),
            ("A.x" , "B.x" , "C.x" , "D.x"),
            ("A.x" , "B.x" , "C.x" , "D.x"),
            ("A.x" , "B.x" , "C.x" , "D.x"))
respuestas = ("A" , "B" , "C" , "D" , "A")
aciertos = []
puntuacion = 0
pregunta_num = 0

for pregunta in preguntas:
    print("SIMULACRO DE EXAMEN"
          "")
    print("--------------------------------")
    print(pregunta)
    for opcion in opciones[pregunta_num]:
        print(opcion)

    acierto = input("Pulsa (A, B, C, D):  ").upper()
    aciertos.append(acierto)
    if acierto == respuestas[pregunta_num]:
        puntuacion += 1
        print("CORRECTO!")
    else:
        print("INCORRECTO!")
        print(f"{respuestas[pregunta_num]} es la respuesta correcta")
    pregunta_num += 1

print("-------------------------")
print("        RESULTADO        ")
print("-------------------------")

print("respuestas= ", end=" ")
for respuesta in respuestas:
    print(respuesta, end=" ")
print()

print("aciertos= ", end= "")
for acierto in aciertos:
    print(acierto, end= "")
print()

puntuacion = int(puntuacion / len(preguntas) * 100)
print(f"Tu puntuacion es: {puntuacion}%")
input()