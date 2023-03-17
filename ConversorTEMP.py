O = int(input('Escolha a unidade a ser convertida: 1 Celsius 2 Fahrenheit 3 Kelvin.  '))

if O == int(1):
    C = int(input('Digite o Valor da Temperatura em Celsius: '))
    ou = int(input('Escolha a unidade para a conversão: 1 Fahrenheit 2 Kelvin.  '))
    if ou == int(1):
        F = int(9/5*(C)+32)
        print('A temperatura em Fahrenheit é: ',F)
        input('Digite enter para fechar o programa: ')
    else:
        K = int(C+273)
        print('A Temperatura em Kelvin é: ',K)
        input('Digite enter para fechar o programa: ')


elif O == int(2):
    F = int(input('Digite o Valor da Temperatura em Fahrenheit: '))
    ou = int(input('Escolha a unidade para a conversão: 1 Celsius 2 Kelvin.  '))
    if ou == int(1):
        C = int((5*(F-32)/9))
        print('A temperatura em Celsius é: ',C)
        input('Digite enter para fechar o programa: ')
    else:
        K = int((5*(F-32)/9)+273)
        print('A Temperatura em Kelvin é: ',K)
        input('Digite enter para fechar o programa: ')


elif O == int(3):
    K = int(input('Digite o Valor da Temperatura em Kelvin: '))
    ou = int(input('Escolha a unidade para a conversão: 1 Celsius 2 Fahrenheit.  '))
    if ou == int(1):
        C = int(K - 273)
        print('A temperatura em Celsius é: ',C)
        input('Digite enter para fechar o programa: ')
    else:
        F = int(9/5*(K-273)+32)
        print('A Temperatura em Kelvin é: ',F)
        input('Digite enter para fechar o programa: ')

