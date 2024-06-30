import random

n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
list = [n1, n2, n3, n4]
random.shuffle(list)  
print('Ordem da apresentação:')
print(list)