from math import radians, sin, cos, tan 

ang = float(input('Digite um ângulo: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(sin, cos, tan))
