lista=[1,2,3,4,5]

n1= int(input("Digite um número:"))

if (n1>0):
    x=lista.extend([n1])
else:
    x= lista.extend([0])

print(lista)