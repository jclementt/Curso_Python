def maior(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max

def menor(x, y, z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
print(f'\nO maior número é: {maior(num1, num2, num3)}')
print(f'O menor número é: {menor(num1, num2, num3)}')
