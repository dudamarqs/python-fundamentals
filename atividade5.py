# Faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
predecessor = n - 1
successor = n + 1
print('O antecessor de {} é {}'.format(n, predecessor))
print('O o sucessor de {} é {}'.format(n, successor))