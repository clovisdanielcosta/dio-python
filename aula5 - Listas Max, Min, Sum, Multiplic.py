lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']


soma = 0
for x in lista:
    print(x)
    soma += x
    print(soma)
#Usando função Sum, Min, Max
print(sum(lista))
print(min(lista))
print(max(lista))

# Vale para strings também Max e Min
print(min(lista_animal))
print(max(lista_animal))

#Multiplicando os valores da lista
nova_lista = lista_animal * 3
print(nova_lista)


