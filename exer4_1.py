lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lista[1:10]) # a)

print(lista[3:14]) # b)

print(lista[2:15:2]) # c)

print(lista[1:16:2]) # d)

multiplos2=[num for num in lista if num % 2 == 0]
multiplos3=[num for num in lista if num % 3 == 0] # e)
multiplos4=[num for num in lista if num % 4 == 0]

print("Múltiplos  de 2:", multiplos2)
print("Múltiplos  de 3:", multiplos3) # e)
print("Múltiplos  de 4:", multiplos4)

lista.reverse()     # f)
print(lista)

lista.reverse()
soma= sum(lista[10:16])     # g)
print(soma)

lista.append(16)        # h)
print(lista)

lista.insert(6, "Marcelo")      # i)
print(lista)