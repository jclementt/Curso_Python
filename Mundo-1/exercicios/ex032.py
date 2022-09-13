from unittest import result


from datetime import date

ano = int(input('Digite um ano para ser analisado ou 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano {ano} é BISSEXTO')
else:
    print(f'O Ano {ano} NÃO é BISSEXTO')
