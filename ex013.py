salario = float(input('Salário do colaborador:R$ '))
aumento = float(input('Qual será o valor do aumento?(%) '))
novosalario = salario + (salario * aumento / 100)
print('O salário do coloborador que era {:.2f}, agora com aumento de {:.2f}% ele ficará {:.2f}'.format(salario, aumento, novosalario))