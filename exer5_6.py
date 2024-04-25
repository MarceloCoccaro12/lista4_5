n1= int(input("Digite um número:"))
n2= int(input("Digite um número:"))
n3= int(input("Digite um número:"))
n4= int(input("Digite um número:"))
n5= int(input("Digite um número:"))
n6= int(input("Digite um número:"))
n7= int(input("Digite um número:"))
n8= int(input("Digite um número:"))
n9= int(input("Digite um número:"))
n10= int(input("Digite um número:"))

lista= [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

multiplos3= [num for num in lista if num % 3 == 0]
menor= [num for num in lista if num < 45]
maior= [num for num in lista if num > 55]
x= min(lista)
media= sum(lista) / len(lista)

print("Múltiplos de  3:", multiplos3)
print("Menores que 45:", menor)
print("maiores que 55", maior)
print("Menor de todos:", x)
print("Média:", media)