print('CALCULAR SEU IMC')
peso = float(input('Qual é seu peso? (KG)'))
altura = float(input('Qual é sua altura? (M)'))
IMC = peso / (altura ** 2)
print('SEU IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do IDEAL.')
elif IMC == 18.5 and IMC <= 25:
    print('Você está com PESO IDEAL.')
elif IMC > 25 and IMC <= 30:
    print('Você está com SOBREPESO.')
elif IMC > 30 and IMC <= 40:
    print('Você está com OBESIDADE.')
elif IMC > 40:
    print('Você está com OBESIDADE MÓRBIDA.')


#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Pes
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
