from random import randint
comp = randint(0,5)
print('-=' * 34)
print('Pensei em um número entre 0 e 5. Veja se consegue descobrir qual é!')
print('-=' * 34)
user = int(input('Em que número eu pensei? >'))
if user == comp:
    print('Você acertou!')
else:
    print('Errado! Pensei no número {} e não no {}!'.format(comp, user))