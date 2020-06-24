a = int(input('Digite o primeiro valor...: '))
b = int(input('Digite o segundo valor...: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(type(soma))
print(subtracao)
print(multiplicacao)
print(divisao)

print('soma: ' + str(soma))
print('Soma: {}. \nSubttração: {}.'.format(soma, subtracao))

print(type(soma))
soma = str(soma)

#Convertendo para inteiro
print(int(divisao))
print(resto)
#Convertendo String em Inteiro
x = '1'
soma2 = int(x) + 1
print(soma2)
# Para comentário de linha # e de bloco ctrl + /
# sdf
# sdfs
# df

# Usando o format para concatenar strings e números
print('soma: {}'.format(soma))
print('Soma: {}. Subttração: {}.'.format(soma, subtracao))
print('Soma: {sm}. Subttração: {sb}.'.format(sm = soma, sb = subtracao))
print('Soma: {sm}. Subttração: {sb}.\n'.format(sm = soma,
                                             sb = subtracao))

resultado = ('Soma: {sm}.\n'
      'Subttração: {sb}.\n'
      'Multiplicação: {mp}.\n'
      'Divisão: {dv}.\n'
      'Resto: {rs}.'
      .format(sm = soma,
              sb = subtracao,
              dv = divisao,
              mp = multiplicacao,
              rs = resto))

print(resultado)