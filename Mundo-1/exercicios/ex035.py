def triangulo(x, y, z):
   if x < (y + z) and y < (x + z) and z < (x + y):
        return 'Podem formar um Triângulo'
   else:
        return 'Não podem formar um Triângulo'

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
print(f'{triangulo(r1, r2, r3)}')
