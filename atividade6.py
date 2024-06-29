# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

number = int(input('Digite um número: '))
double = number * 2
triple = number * 3
square_root = number ** 0.5
print('\n')
print('Dobro de {}: {}'.format(number, double))
print('Triplo de {}: {}'.format(number, triple))
print('Raíz quadrada de {}: {}'.format(number, square_root))