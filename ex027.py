name = str(input('Qual o seu nome completo? ')).strip()
nome = name.split()
print('Muito prazer em te conhecer, {}!'.format(name))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))


