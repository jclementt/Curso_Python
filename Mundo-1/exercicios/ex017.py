from math import hypot

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
h = hypot(co, ca)
print('\nUtilizando o Teorema de Pitágoras, temos:')
print('Cateto Oposto = {:.2f}\nCateto Adjacente = {:.2f}\nHipotenusa = {:.2f}\n'.format(co, ca, h))
