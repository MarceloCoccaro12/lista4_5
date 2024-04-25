for i in range(20):
    a=int(input("Digite um valor:"))
    b=int(input("Digite um valor:"))
    c=int(input("Digite um valor:"))

    if (a>b) and (a>c):
        maior="A"
    elif (b>a) and (b>c):
        maior="B"
    else:
        maior="C"

    print("O maior entre eles é:", maior)
 
