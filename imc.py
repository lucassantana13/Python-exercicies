while True:
    peso = float(input('insira o valor do seu peso em KG: '))
    altura = float(input('insira o valor do sua altura em metros: '))
    imc = peso / (altura*altura)
    if imc<16:
        print (f'Seu IMC é de {imc:.1f}. Índice de magreza grau III.')
    elif imc>=16 and imc<17:
        print (f'Seu IMC é de {imc:.1f}. Índice de magreza grau II.')
    elif imc>=17 and imc<18.5:
        print (f'Seu IMC é de {imc:.1f}. Índice de magreza grau I.')
    elif imc>=18.5 and imc<25:
        print (f'Seu IMC é de {imc:.1f}. Índice de eutrofia, (peso normal).')
    elif imc>=25 and imc<30:
        print (f'Seu IMC é de {imc:.1f}. Índice de pré-obesidade(sobrepeso).')
    elif imc>=30 and imc<35:
        print (f'Seu IMC é de {imc:.1f}. Índice de obesidade moderada (grau I)')
    elif imc>=35 and imc<40:
        print (f'Seu IMC é de {imc:.1f}. Índice de obesidade severa (grau II).')
    elif imc>=40:
        print (f'Seu IMC é de {imc:.1f}. Índice de obesidade muito severa (grau III).')
    if input('Quer continuar? (S/N) ') == 'n' or 'N':
        
        break 
    elif input('Quer continuar? (S/N) ') == 's' or 'S':
        continue