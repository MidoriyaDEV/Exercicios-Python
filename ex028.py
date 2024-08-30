from random import randint
from time import sleep
computador = randint(0, 10) # faz computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('NICE!!! Você acertou.')
else:
    print('Não foi dessa vez..., Eu pensei no número {} e não no {}!'.format(computador, jogador))



