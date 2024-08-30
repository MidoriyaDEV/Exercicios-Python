from time import sleep
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO! você excedeu o limite de 80km/h')
    multa = (velocidade - 80) * 7
    sleep(3)
    print('A multa vai custar R$7,00 por cada Km acima do limite.')
    sleep(3)
    print('você deve pagar a multa de R${:.2f}!'.format(multa))
else:
    print('Dirija com segurança!')

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
#Km acima do limite.