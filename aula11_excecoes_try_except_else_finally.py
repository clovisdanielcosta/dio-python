lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    divisao = 10 / 0
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possível dividir por Zero')
except IndexError:
    print('Índice da lista não existe.')
# Para tratar exceções não previstas. BaseException é o Pai de todas as Exceções
# Pode usar também 'Exception' apenas.
# Colocar sempre no topo as exceções filhos
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa quando não há erros de exceções.')
finally:
    print('Sempre executa, mesmo se der erros.')
    print('Fechando o arquivo...')
    arquivo.close()