conjunto = {1, 2, 3, 4}
print(type(conjunto))
print(conjunto)

#Não se repete. São elementos únicos
conjunto2 = {1, 2, 3, 4, 4, 2}
print(conjunto2)

# Adicionando
conjunto.add(5)
print(conjunto)

# Eliminando
conjunto.discard(2)
print(conjunto)
