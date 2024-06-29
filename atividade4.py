# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo é', type(a))
print('Somente espaço?', a.isspace())
print('São somente letras?', a.isalpha())
print('Está totalmente em letras maiúsculas?', a.isupper())
print('Está totalmente em letras minúsculas?', a.islower())
print('É alfanumérico?', a.isalnum())
print('Está capitalizada (maiúsculas e minúsculas)?', a.istitle())
