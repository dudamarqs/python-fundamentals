n = str(input('Digite seu nome completo: ')).strip()
name = n.split()
print('"{}" é o seu primeiro nome.'.format(name[0]))
print('"{}" é o seu último nome.'.format(name[len(name)-1]))