a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O maior valor é: {}'.format(a))
else:
    print('O maior valor é: {}'.format(b))
print('Fim do programa')

#Usando Elif (Else If)
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior valor é: {}'.format(a))
elif b > a and b > c:
    print('O maior valor é: {}'.format(b))
else:
    print('O maior valor é: {}'.format(c))
print('Fim do programa')
