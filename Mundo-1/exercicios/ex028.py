from random import randint

numb_computer = randint(0, 5)
print(numb_computer)
print('Bem vindo(a) ao Jogo TENTE DESCOBRIR!')
print('-=-' * 20)
print("""O nosso programa gerou um número aleatório entre 0 e 5...
        O seu objetivo é adivinhar qual é o número sorteado.
        Vamos lá, você aceita participar do JOGO?""")
print('-=-' * 20)
resp = str(input('Se sim digite SIM, se não digite NÃO: ')).lower()
if resp == 'sim':
    print('Fico feliz por querer participar! Agora é com você.')
    numb_user = int(input('Escolha um número de 0 a 5: '))
    if numb_computer == numb_user:
        print('Parabéns, você acertou!!!!')
    else:
        print('Poxa, não foi dessa vez. Na próxima você terá mais sorte!')
else:
    print('Então isso é um Adeus!')
