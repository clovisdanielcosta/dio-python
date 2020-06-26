conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

# Diferença
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

#Diferença Simétrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica entre 1 e 2: {}'.format(conjunto_diff_simetrica))
