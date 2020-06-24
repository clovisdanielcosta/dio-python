#Descobrindo os números primos em um range
a = int(input('Digite o primeiro bimestre: '))
while a > 10:
    a = int(input('Nota inválida! Digite o primeiro bimestre: '))

b = int(input('Digite o segundo bimestre: '))
while b > 10:
    b = int(input('Nota inválida! Digite o segundo bimestre: '))

c = int(input('Digite o terceiro bimestre: '))
while c > 10:
    c = int(input('Nota inválida! Digite o terceiro bimestre: '))

d = int(input('Digite o quarto bimestre: '))
while d > 10:
    d = int(input('Nota inválida! Digite o terceiro bimestre: '))

media = print((a + b + c + d) / 4)