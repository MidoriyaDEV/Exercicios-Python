nome = str(input('Qual é seu nome? '))
if nome == 'João':
    print('Que nome lindo!')
elif nome == 'Enzo' or nome == 'Maria':
    print('Seu nome é bastante bonito.')
else:
    print('Prazer em te conhecer!')
print('Tenha um Bom dia, {}'.format(nome))


