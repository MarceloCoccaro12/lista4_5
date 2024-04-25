for i in range(10):
    num=int(input("Digite um número:"))
    
    if (num > 0):
        print("É positivo")
    elif (num == 0):
        print("É igual a zero")
    else:
        print("É negativo")
    
    if (num % 3 == 0):
        print("É múltiplo de 3")
    else:
        print("Não é múltiplo de 3")