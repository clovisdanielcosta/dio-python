# As variáveis abaixo estão recebendo uma função anônima
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(10, 5))
print(subtracao(10, 5))

# Dicionário de Lambda
calculadora = {
    'somar': lambda a, b: a + b,
    'subtrair': lambda a, b: a - b,
    'multiplicar': lambda a, b: a * b,
    'dividir': lambda a, b: a / b,
}

somando = calculadora['somar']
subtraindo = calculadora['subtrair']
multiplicando = calculadora['multiplicar']
dividindo = calculadora['dividir']

print('A soma é: {}'.format(somando(10, 9)))
print('A divisão é: {}'.format(dividindo(100, 3)))
