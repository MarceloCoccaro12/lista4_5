for i in range(30):
    p1= float(input("Digite sua nota:"))
    p2= float(input("Digite sua nota:"))

    media= p1 + p2 / 2

    if (media >=5):
        print("APROVADO")
    elif(media >=3) and (media < 5):
        print("EXAME")
        nota= float(input("Digite sua nota:"))
        
        if (nota >= 5):
            print("APROVADO")
        else:
            print("REPROVADO")
    else:
            print("REPROVADO")

    
