import time
from datetime import date
print('-=-'*20)
print('                SERVIÇO DE ALISTAMENTO        ')
print('-=-'*20)
Nascimento = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = atual - Nascimento
if idade < 18:
    Saldo = 18 - idade
    print('Você ainda não tem 18 anos para se alistar.')
    print('Falta {} ano para você se alistar'.format(Saldo))
elif idade == 18:
    print('Processando....')
    time.sleep(3)
    print('Você tem que se Alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você deve comparecer a junta militar!')
    print('Você passou do tempo de alistamento.')

#Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


