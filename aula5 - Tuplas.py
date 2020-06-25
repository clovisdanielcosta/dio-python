lista = [1, 13, 15, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'arara']

print(lista_animal)
#Alterando valor da lista
lista_animal[0] = 'macaco'
print(lista_animal)

#TUPLAS
# Não pode ser alterada
print(lista)
tupla = (1, 13, 15, 7)
print(tupla)
# tupla[0] = 12
#TypeError: 'tuple' object does not support item assignment

#Verificando o tamanho da lista e da tupla
print(len(lista_animal))
print(len(tupla))
