dias = int(input('Quantos dias o carro foi alugado? '))
km= float(input('Quantos km rodados? '))
print(' O total a pagar é: {}R$'.format(dias * 60 + km))
calculo = (dias * 60) + (km * 0.15)
