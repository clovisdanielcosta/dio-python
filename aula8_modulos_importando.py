# Importando Classes
from aula7_classes_televisao import Televisao
from aula7_classes_calculadora2 import Calculadora

# Importando Método
from aula8_metodos_contador_letras import contador_letras, teste

televisao = Televisao()
calc = Calculadora()
lista = ['cachorro', 'galinha', 'papagaio']

print(televisao.ligada)
televisao.power()
print(televisao.ligada)
print(calc.soma(15, 2))

total_letras = contador_letras(lista)
print('Total de letras de cada palavra: {}'.format(total_letras) )
print(teste())