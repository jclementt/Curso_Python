km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias o carro foi alugado? '))
total = (60 * dias) + (0.15 * km)
print('Dias alugado = {}\nKm rodados = {:.1f}\nPreço a pagar = R${:.2f}'.format(dias, km, total))
