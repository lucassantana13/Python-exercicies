#entrada

conta = input('Digite o numero da conta: ')
senha = input('Digite a senha da conta: ')

#Banco de dados

bc01 = ('10101')
bc02 = ('20202')
bc03 = ('30303')
bc04 = ('40404')
sbc01 = ('1111')
sbc02 = ('2222')
sbc03 = ('3333')
sbc04 = ('4444')
sld01 = int(504.52)
sld02 = int(34.2)
sld03 = int(224.5)
sld04 = int(69.90)

#processamento

if conta == bc01 and senha == sbc01:
    print ('seu saldo é de: R$',sld01)
    operacao = input('Digite 1 para sacar ou 2 para depositar: ')
    if operacao == '2':
        dep = int(input('digite o valor a ser depositado: '))
        input('insira o envelope e aperte enter: ')
        sld01n = (dep+sld01)
        print('O novo saldor é de: R$',sld01n)
        input('aperte enter para encerrar a transação: ')
    elif operacao == '1':
        saq1 = int(input(('Digite o Valor a ser sacado: ')))
        if int((saq1%2) == 0):

            saq = saq1

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            dois = int(saq/2)
            saq = saq - (dois*2)
        else:
            saq = saq1

            saq = saq - 5

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)

            dois = int(saq/2)
            saq = saq - (dois*2)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            

            cinc = cinc+1
    print('Notas R$100,00 = ',cem)
    print('Notas R$50,00 = ',cinq)
    print('Notas R$20,00 = ',vint)
    print('Notas R$10,00 = ',dez)
    print('Notas R$5,00 = ',cinc)
    print('Notas R$2,00 = ',dois)
    nvsld = (sld01 - saq1)
    print(f'Seu novo saldo é de `{nvsld}')
    input('aperte enter para encerrar a transação: ')

if conta == bc02 and senha == sbc02:
    print ('seu saldo é de: R$',sld02)
    operacao = input('Digite 1 para sacar ou 2 para depositar: ')
    if operacao == '2':
        dep = int(input('digite o valor a ser depositado: '))
        input('insira o envelope e aperte enter: ')
        sld02n = (dep+sld02)
        print('O novo saldor é de: R$',sld02n)
        input('aperte enter para encerrar a transação: ')
    elif operacao == '1':
        saq1 = int(input(('Digite o Valor a ser sacado: ')))
        if int((saq1%2) == 0):

            saq = saq1

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            dois = int(saq/2)
            saq = saq - (dois*2)
        else:
            saq = saq1

            saq = saq - 5

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)

            dois = int(saq/2)
            saq = saq - (dois*2)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            

            cinc = cinc+1
    print('Notas R$100,00 = ',cem)
    print('Notas R$50,00 = ',cinq)
    print('Notas R$20,00 = ',vint)
    print('Notas R$10,00 = ',dez)
    print('Notas R$5,00 = ',cinc)
    print('Notas R$2,00 = ',dois)
    nvsld = (sld02 - saq1)
    print(f'Seu novo saldo é de `{nvsld}')
    input('aperte enter para encerrar a transação: ')

if conta == bc03 and senha == sbc03:
    print ('seu saldo é de: R$',sld03)
    operacao = input('Digite 1 para sacar ou 2 para depositar: ')
    if operacao == '2':
        dep = int(input('digite o valor a ser depositado: '))
        input('insira o envelope e aperte enter: ')
        sld03n = (dep+sld03)
        print('O novo saldor é de: R$',sld03n)
        input('aperte enter para encerrar a transação: ')
    elif operacao == '1':
        saq1 = int(input(('Digite o Valor a ser sacado: ')))
        if int((saq1%2) == 0):

            saq = saq1

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            dois = int(saq/2)
            saq = saq - (dois*2)
        else:
            saq = saq1

            saq = saq - 5

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)

            dois = int(saq/2)
            saq = saq - (dois*2)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            

            cinc = cinc+1
    print('Notas R$100,00 = ',cem)
    print('Notas R$50,00 = ',cinq)
    print('Notas R$20,00 = ',vint)
    print('Notas R$10,00 = ',dez)
    print('Notas R$5,00 = ',cinc)
    print('Notas R$2,00 = ',dois)
    nvsld = (sld03 - saq1)
    print(f'Seu novo saldo é de `{nvsld}')
    input('aperte enter para encerrar a transação: ')

if conta == bc04 and senha == sbc04:
    print ('seu saldo é de: R$',sld04)
    operacao = input('Digite 1 para sacar ou 2 para depositar: ')
    if operacao == '2':
        dep = int(input('digite o valor a ser depositado: '))
        input('insira o envelope e aperte enter: ')
        sld04n = (dep+sld04)
        print('O novo saldor é de: R$',sld04n)
        input('aperte enter para encerrar a transação: ')
    elif operacao == '1':
        saq1 = int(input(('Digite o Valor a ser sacado: ')))
        if int((saq1%2) == 0):

            saq = saq1

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            dois = int(saq/2)
            saq = saq - (dois*2)
        else:
            saq = saq1

            saq = saq - 5

            cem = int(saq/100)
            saq = saq - (cem*100)
            
            cinq = int(saq/50)
            saq = saq - (cinq*50)
            
            vint = int(saq/20)
            saq = saq - (vint*20)
            
            dez = int(saq/10)
            saq = saq - (dez*10)

            dois = int(saq/2)
            saq = saq - (dois*2)
            
            cinc = int(saq/5)
            saq = saq - (cinc*5)
            
            

            cinc = cinc+1
    print('Notas R$100,00 = ',cem)
    print('Notas R$50,00 = ',cinq)
    print('Notas R$20,00 = ',vint)
    print('Notas R$10,00 = ',dez)
    print('Notas R$5,00 = ',cinc)
    print('Notas R$2,00 = ',dois)
    nvsld = (sld04 - saq1)
    print(f'Seu novo saldo é de R${nvsld}')
    input('aperte enter para encerrar a transação: ')




