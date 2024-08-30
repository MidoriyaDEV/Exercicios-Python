from time import sleep
distancia = int(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0,50
    print('Foi cobrado uma taxa de R$0,50')
    sleep(3)
    print('O valor a pagar pela viagem foi {:.2f}R$'.format(preco))
else: #distância maior que 200KM
    preco = distancia * 0.45
    print('Foi cobrado uma taxa de R$0,45')
    sleep(3)
    print('O valor a pagar é {:.2f}R$'.format(preco))


#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 parta viagens mais longas.

