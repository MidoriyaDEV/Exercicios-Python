from datetime import date
print('-=-'*20)
print('             Confederação Nacional de Natação')
print('-=-'*20)
Nascimento = int(input('Qual ano você nasceu: '))
Atual = date.today().year
idade = Atual - Nascimento
print('Sua idade é {}'.format(idade))
if idade <= 9:
    print('Você tem idade para categoria MIRIM')
elif idade >= 10 and idade <= 14:
    print('Você tem idade para categoria INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Você tem idade para categoria JÚNIOR')
elif idade >= 20 and idade <= 25:
    print('Você tem idade para categoria SÊNIOR')
else:
    print('Você tem idade para categoria MASTER')



#A Confederação Nacional de Natação precisa de um 
#programa que leia o ano de nascimento de um atleta 
#e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
