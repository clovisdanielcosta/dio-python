conjunto = {1, 2, 3,}
conjunto2 = {1, 2, 3, 5, 6}

# Pertinência

# Subset: verifica se o primeiro conjunto é subconjunto do segundo
conj_subset = conjunto.issubset(conjunto2)
print('Conjunto é um Sub Conjunto de Conjunto2: {}'.format(conj_subset)) # False
# Superset: Verifica se o primeiro é Superconjunto do segundo
conj_superset = conjunto2.issuperset(conjunto)
print('Conjunto2 é um Super Conjunto de Conjunto: {}'.format(conj_superset)) # True