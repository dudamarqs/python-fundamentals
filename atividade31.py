distance = float(input('Qual a distância da sua viagem (em km)? '))
if distance <= 200:
    print('A passagem vai custar R${:.2f}.\n'.format(distance * 0.5))
else:
    print('A passagem vai custar R${:.2f}.\n'.format(distance * 0.45))