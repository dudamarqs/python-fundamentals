price = float(input('Digite o preço do produto: R$'))
sale = price - (price * 0.05)
print('Com o desconto de 5%, o produto que custa R${:.2f} vai custar R${:.2f} na promoção.'.format(price, sale))