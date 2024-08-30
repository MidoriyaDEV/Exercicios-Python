Produto = float(input('Digite o valor do produto: R$ '))
Desconto = float(input('Digite o valor do desconto (%): '))
DescontoRES = Desconto*Produto / 100
DESCONTOREAL = Produto-DescontoRES
print('O produto que custava {:.2f}R$ agora custa {:.2f}R$ com o desconto de {:.2f}%'.format(Produto, DESCONTOREAL, Desconto))


