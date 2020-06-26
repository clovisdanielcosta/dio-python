# As variáveis abaixo estão recebendo uma função anônima
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'pato', 'marreco']
print(contador_letras(lista_animais))
