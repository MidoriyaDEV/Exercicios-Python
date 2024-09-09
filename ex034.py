salario_bruto = int(input('Quanto é seu salário bruto:R$ '))
if salario_bruto > 1250:
    salario_liquido = salario_bruto * 10/100 + salario_bruto
else:
    salario_liquido = salario_bruto * 15/100 + salario_bruto

print('Quem ganhava {:.2f}R$ agora com aumento irá receber {:.2f}R$'.format(salario_bruto, salario_liquido))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
# aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.