from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('O comprimento da hipotenusa é aproximadamente igual a {:.2f}.'.format(hip))
