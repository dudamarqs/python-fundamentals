# O carro custa R$60,00 por dia.
# R$0,15 por km rodado.

days = int(input('Por quantos dias o carro foi alugado? '))
km = float(input("Informe a quantidade de Km rodados: "))
price_to_pay = (days * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}.'.format(price_to_pay)) 