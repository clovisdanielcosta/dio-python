lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

#Verificando elemento dentro da lista
if 'lobo' in lista_animal:
    print('Existe lobo na lista.')
else:
    #Incluindo na lista
    print('Não existe lobo na lista. Será incluído.')
    lista_animal.append('lobo')
    print(lista_animal)

#Removendo da lista
lista_animal.pop()
print(lista_animal)

#Removendo pelo nome
lista_animal.remove('elefante')
print(lista_animal)

#Removendo pelo índice
lista_animal.pop(1)
print(lista_animal)
