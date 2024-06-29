# Desenvolva um programa que leia um valor em metros e o exiba convertido em milímetros.

number = float(input('Digite um valor em metros: '))
km = number / 1000
hm = number / 100
dam = number / 10
dm = number * 10
cm = number * 100
mm = number * 1000
print('{:.0f} m equivale a: \n{} km \n{:.0f} hm \n{:.0f} dam \n{:.0f} dm \n{:.0f} cm \n{:.0f} mm'.format(number, km, hm, dam, dm, cm, mm))