frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira ocorrência de A está na posição {}.'.format(frase.find('A')+1))
print('A ultima corrência de A está na posição {}.'.format(frase.rfind('A')+1))
