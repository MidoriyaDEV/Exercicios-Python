print('-=-'*20)
print('              Analisando um Triangulo')
print('-=-'*20)
R1 = float(input('Primeiro segmento: '))
R2 = float(input('Segundo segmento: '))
R3 = float(input('Terceiro segmento: '))
if R1 < R2+R3 and R2 <R1+R3 and R3 < R1+R2:
    print('O segmentos acima pode formar um triangulo.', end='')
    if R1 == R2 == R3:
        print('EQUILÁTERO')
    elif R1 != R2 != R3 != R1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
        

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ESCALENO: todos os lados diferentes
#– ISÓSCELES: dois lados iguais, um diferente
