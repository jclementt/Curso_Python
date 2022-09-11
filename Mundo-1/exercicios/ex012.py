prod = float(input('Preço do produto: '))
desc = prod - (prod * 5 / 100)
print('O valor do produto com desconto de 5% é: R$ {:.2f}'.format(desc))
