# código ANSI ascape sequence
#cores no terminal

# Style: Estilo da letra --> \033["style";text;backm
# 0 = none (nenhum)
# 1 = bold (negrito)
# 4 = underline (sublinhado)
# 7 = negativo (inverte a cor da letra e do fundo)

# Text: Cor do texto --> \033[style;"text";backm
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul escuro
# 35 = roxo
# 36 = azul claro
# 37 = cinza

# Back: Cor de fundo --> \033[style;text;"back"m
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul escuro
# 45 = roxo
# 46 = azul claro
# 47 = cinza

#Exemplo: \033[2;36;40m

#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m

print('\033[1;31;46mMódulo 1 completo!\033[m')
a = 23
b = 25
print(f'Os valores são: \033[1;31m{a}\033[m \033[1;33m{b}\033[m!!!')
nome = 'Joanna'
print('Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

