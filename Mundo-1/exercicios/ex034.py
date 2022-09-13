salary = float(input('Digite seu em R$: '))
if salary > 1250:
    increase10 = salary + (salary * 10 / 100)
    print(f'Seu salário com 10% de aumento: R$ {increase10:.2f}')
else:
    increase15 = salary + (salary * 15 / 100)
    print(f'Se salário com 15% de aumento: R$ {increase15:.2f}')
