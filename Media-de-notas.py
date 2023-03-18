#entrada
nota1 = int(input('insira nota 1: '))
nota2 = int(input('insira nota 2: '))
nota3 = int(input('insira nota 3: '))

#processsamento
mediafinal = (nota1+nota2+nota3)/3

if mediafinal>=6:
    print ('aprovado')
else:
    print('reprovado')
