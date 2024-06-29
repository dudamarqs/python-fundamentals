# Crie um programa que leia quanto dinheiro uma pessoa tem (em reais) e mostre quantos dólares e euros é possível comprar.
# Considere U$S = 5,59
# Considere € = 5,99

real = float(input('Quantos reais você tem? \nR$ '))
dolar = real / 5.59
euro = real / 5.99
print('Com R${:.2f} você pode comprar US${:.2f} e {:.2f}€.'.format(real, dolar, euro)) 