sentence = str(input('Escreva uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes na frase.'.format(sentence.count('a')))
print('A 1ª letra "A" apareceu na {}ª posição.'.format(sentence.find('a')+1))
print('A última letra "A" apareceu na {}ª posição.'.format(sentence.rfind('a')+1))
