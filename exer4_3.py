n1= float(input("Digite sua nota:"))
n2= float(input("Digite sua nota:"))
n3= float(input("Digite sua nota:"))
n4= float(input("Digite sua nota:"))

notas=[n1,n2,n3,n4]

media= sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)