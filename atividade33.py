a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Verificando o menor valor 
sma = a
if b<a and b<c:
    sma = b
if c<b and c<a:
    sma = c
# Verificando o maior valor
big = b
if a>c and a>b:
    big = a
if c>a and c>b:
    big = c
print('\nO menor número é {}.'.format(sma))
print('O maior número é {}.'.format(big))