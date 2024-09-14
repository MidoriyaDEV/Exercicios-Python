number = int(input('Digite um número qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number, oct(number)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number, hex(number)))
else:
    print('Opção inválida. Tente novamente.')

#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

