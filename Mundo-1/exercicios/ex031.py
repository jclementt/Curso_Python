km = int(input('Informe a distância da sua viagem em km: '))
if km > 200:
    value1 = km * 0.45
    print(f'O valor da sua passagem é R$ {value1:.2f}')
else:
    value2 = km * 0.50
    print(f'O valor da sua passagem é R$ {value2:.2f}')
