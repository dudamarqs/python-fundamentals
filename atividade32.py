year = int(input('Digite o ano qualquer e veja se ele é bissexto: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('O ano é {} é bissexto.\n'.format(year))
else:
    print('O ano {} não é bissexto.'.format(year))