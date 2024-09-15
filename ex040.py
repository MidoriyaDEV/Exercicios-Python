N1 = int(input('Digite a primeira nota: '))
N2 = int(input('Digite a segunda nota: '))
Media = (N1 + N2) / 2
print('Sua Média total foi {:.1f}'.format(Media))
if 7 > Media >= 5:
    print('Você está de RECUPERAÇÃO')
elif Media >= 7:
    print('Você está APROVADO')
elif Media < 5:
    print('Você está REPROVADO!')



#Crie um programa que leia duas notas de um aluno e calcule 
#sua média, mostrando uma mensagem no final, 
#de acordo com a média atingida:
#Média abaixo de 5.0: REPROVAD
