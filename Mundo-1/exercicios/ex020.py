from random import shuffle

aluno1 = str(input('Digite o nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o nome do Segundo Aluno: '))
aluno3 = str(input('Digite o nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o nome do Quarto Aluno: '))
nomes = [aluno1, aluno2, aluno3, aluno4]
shuffle(nomes)
print('A ordem da apresentação foi: {}'.format(nomes))