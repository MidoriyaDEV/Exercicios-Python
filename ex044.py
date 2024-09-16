print('{:=^40}'.format(' LOJAS VITTOR '))
produto = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque:
[ 2 ] à vista no cartão:
[ 3 ] até 2x no cartão:
[ 4 ] 3x ou mais no cartão:''')
options = int(input('Qual é a opção? '))
if options == 1:
    total = produto - (produto * 10 / 100)
elif options == 2:
    total = produto - (produto * 5 / 100)
elif options == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcela, total))
elif options == 4:
    total = produto + (produto * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparc, parcela))
else:
    print('ERROR - CODIGO INVALIDO')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, total))

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

