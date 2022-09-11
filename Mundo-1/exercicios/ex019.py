from random import choice

aluno1 = str(input('Digite o nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o nome do Segundo Aluno: '))
aluno3 = str(input('Digite o nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o nome do Quarto Aluno: '))
nomes = aluno1, aluno2, aluno3, aluno4
def selectRandom(nomes):
    return choice(nomes)
print('O Aluno escolhido para apagar o quadro foi: {}'.format(selectRandom(nomes)))
