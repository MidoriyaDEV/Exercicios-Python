Casa = float(input('Valor da casa: R$'))
Salario = int(input('Salario do comprador: R$'))
Anos = int(input('Quantos anos de financiamento? '))
Prestação = Casa / (Anos * 12)
Minimo = Salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(Casa, Anos), end ='')
print('a prestão será de R${:.2f}'.format(Prestação))

print('COMPARANDO tem que pagar {:.2f} e o mínimo é de  {:.2f}'.format(Prestação, Minimo))


#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
