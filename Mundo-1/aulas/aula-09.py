frase = 'Curso em Video Python'

#Fatiamento
print(frase[9]) #Vai mostrar na tela apenas o caracter que está na posição 9
print(frase[9:13]) #Vai mostrar na tela o caracter que estar na posição 9 até a posição 12
print(frase[9:21:2]) #Vai mostrar na tela os caracter da posição 9 até a posição 20 pulando de 2 em 2
print(frase[:5]) #Vai mostrar na tela o inicio da strig até o caracter na posição 4
print(frase[15:]) #Vai mostrar na tela o caracter na posição 15 até o final da string
print(frase[9::3]) #Vai mostrar na tela o caracter na posição 9 até o final da string pulando de 3 em 3

#Análise
len(frase) #retorna o tamanho da string
frase.count('o') #retorna quantas vezes o caracter 'o' aparece na string
frase.count('o', 0, 13) #retorna quantas vezes o caracter 'o' aparece na string no intervalo selecionado
frase.find('deo') #Retorna a posição da primeira ocorrência da palavra 'deo'
frase.find('Android') #Caso a palavra não for encontrada, o retorno é false -1

#Operador
'Curso' in frase #Retorna TRUE ou FALSE

#Transformação
frase.replace('Python', 'Android')
frase.upper() #transforma os caracteres minusculos em MAIUSCULOS
frase.lower() #transforma os caracteres MAIUSCULOS em minusculos
frase.capitalize() #transforma todos os caracteres MAIUSCULOS em minusculos e deixa apenas o primeiro MAIUSCULO
frase.title() #Analisa quantas palavras tem na string e aplica o capitalize em cada palavra
frase.strip() #remove os espaços inúteis no início e no final da string
frase.rstrip() #remove os espaços inúteis apenas da direita (final da string)
frase.lstrip() #remove os espaços inúteis apenas da esquerda (início da string)

#Divisão
frase.split() #Divide as strig de acordo com os espaços, retorna cada palavra separadamente (em forma de lista)

#Junção
'-'.join(frase) #junta as palavras da string e coloca '-' no lugar dos espaços

