def calcular_C():
    k = int(input("Ingresa el valor de k: "))
    n = int(input("Ingresa el valor de n: "))
    M = int(input("Ingresa el valor de M (mensaje a cifrar): "))
    
    C = (M ** k) % n
    
    print(f"C = ({M}^{k}) % {n} = {C}")

calcular_C()
input()