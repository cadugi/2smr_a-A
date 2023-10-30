def cifrar_M():
    k = int(input("Ingresa el valor de k: "))
    n = int(input("Ingresa el valor de n: "))
    C = int(input("Ingresa el valor de C (mensaje cifrado): "))
    
    # Desciframos el mensaje C
    M = (C ** (1 / k)) % n
    
    print(f"M = ({C}^(1/{k})) % {n} = {M}")

cifrar_M()
input()