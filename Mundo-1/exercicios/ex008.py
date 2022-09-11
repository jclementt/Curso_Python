medida = float(input('Digite uma medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('{}m equivale a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
