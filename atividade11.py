print('Informe as medidas da parede (em metros):')
height = float(input('Altura: '))
width = float(input('Largura: '))
area = height * width
paint = area / 2
print('\nA parede tem a dimesão de {} x {} e sua área equivale a {}m².'.format(height, width, area))
print('Será necessário {}L de tinta para pintar a parede.\n'.format(paint))