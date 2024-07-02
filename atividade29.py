speed = float(input('Qual a velocidade atual do automóvel? '))
if speed <= 80.0:
    print('A velocidade está adequada. Tenha um bom dia!\n')
else:
    fine = (speed - 80) * 7 # Calculates the fine.
    print('Você está acima do limite de velocidade e deverá pagar uma multa de R${:.2f}\n'.format(fine))