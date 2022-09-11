alt = float(input('Altura em metros: '))
lar = float(input('Largura em metros: '))
area = (alt * lar)
qt = area / 2
print('Para pintar uma parede de {:.2f}m² é necessário {:.2f}l de tinta.'.format(area, qt))
