vel = int(input('Velocidade do veículo em km/h: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você recebeu uma multa de RS {multa:.2f} por estar acima do limite permitido.')
else:
    print('Você não possui multas!')
