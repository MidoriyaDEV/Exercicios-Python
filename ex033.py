a1 = int(input('Primeiro valor: '))
a2 = int(input('Segundo valor: '))
a3 = int(input('Terceiro valor: '))
maior = 0
menor = 0
#Descobrir maior e menor
#Verificando quem é o menor valor
menor = a1
if a2 < a1 and a2 < a3:
    menor = a2
if a3 < a1 and a3 < a2:
    menor = a3
#Verificando quem é o maior valor
maior = a1
if a2 > a1 and a2 > a3:
    maior = a2
if a3 > a1 and a3 > a2:
    maior = a3
#Mostrar maior e menor
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
