from math import sin, cos, radians

angle = float(input('Informe o ângulo: '))
sin = sin(radians(angle))
print('\nSeno de {}: {:.2f}'.format(angle, sin))
cos = cos(radians(angle))
print('Cosseno de {}: {:.2f}'.format(angle, cos))