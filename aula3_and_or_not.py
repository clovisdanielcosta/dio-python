a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 and resto_b == 0:
    print('Os valores são pares')
elif resto_a == 0 or resto_b == 0:
    print('Pelo menos um valor é par.')
elif not resto_a == 0 or not resto_b == 0:
    print('Nenhum valor é par.')