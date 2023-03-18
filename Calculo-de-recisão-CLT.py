# Entrada de dados 
d1 = input('Insira a data de admissão ex (dd/mm/aaa): ')
d2 = input('Insira a data de demissão ex (dd/mm/aaa): ')
jc = input('A demissão foi por justa causa? (S/N): ')
ap = input('Você trabalhou o período de aviso prévio? (S/N): ')
fv = input('Você tinha férias vencidas? (S/N): ')
f = ('%d/%m/%Y')
sal = float(input('Insira o salário base mensal: '))

#Conversão de string em data

from datetime import datetime, timedelta

d1  = datetime.strptime(d1, f)
d2  = datetime.strptime(d2, f)

ttrab = d2 - d1 
ttrab = ttrab.days

ttrabmensal = ttrab//30
dias_de_saldo = ((ttrab%365)%30)

#calculos de salários

saldia = sal/30

saldec = sal/12

if (ttrab//30) <= 1:
    saldo_de_salario =(ttrab%30)*(saldia)
elif (ttrab//30) > 1:
    saldo_de_salario = (d2.day)*(saldia)




#Calculo de décimo terceiro
if ((ttrab%365)%30) > 15:
    total_decimo = (d2.month)*(saldec)
else:
    total_decimo = ((d2.month)-1)*(saldec)

#Férias

feprop = ((ttrab%365)//30)*(sal/12)
if ((ttrab%365)%30) > 15:
    feprop = feprop + (sal/12)


umterco = feprop/3

ferias = feprop + umterco

if (fv == 's' or fv == 'S') and (ttrab//365) >= 1:
    feriasn = ferias + sal + (sal/3) 
else:
    feriasn = ferias

# Saída
ap1 = 0

if ap == 's' or ap == 'S':
    ap1 = 0
elif ap == 'n' or ap == 'N':
    ap1 = ((sal/30)*36) + (sal/12) + ((sal/12)/3) +(sal/12)

jc1 = 0

if jc == 's' or jc == 'S':
    feriasn = 0
    total_decimo = 0
    jc1 = 0



vreceber = feriasn+total_decimo+saldo_de_salario+ap1+jc1

print(f'Você temm a receber R${feriasn:.2f}  pelo cálculo de férias; R${total_decimo:.2f}  pelo cálculo de 13º; R${saldo_de_salario+ap1:.2f}  pelo calculo de salários ; e R${jc1:.2f} , por indenizações.')

print(f'O Valor total à ser recebido é de: R${vreceber:.2f}')

print('Este programa é um serviço gratuito que se propõe a auxiliar o usuário como simples referência e verificação de cálculos diversos. Este serviço não deve ser utilizado em substituição a um profissional habilitado. O usuário que utiliza os nossos serviços o faz por sua conta e risco, e aceita que não temos qualquer responsabilidade por danos de qualquer natureza resultantes desta utilização. ')

input('Digite enter para fechar o programa: ')