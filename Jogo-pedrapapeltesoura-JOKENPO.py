import random

opcoes = ['Pedra','Papel','Tesoura']

rep = '1'

while rep == '1':
    jog = int(input('Escolha sua jogada: (1) Pedra.   (2) Papel.   (3) Tesoura.   '))
    bot = random.choice(opcoes)
    
    if jog == 1:
        jog = 'Pedra'
    elif jog == 2:
        jog = 'Papel'
    elif jog == 3:
        jog = 'Tesoura'
    elif jog != 1 or jog != 2 or jog != 3:
        print('Digite um número entre 1, 2 ou 3: ')
    if jog == bot:
        print(f'Você escolheu {jog} e o computador escolheu {bot}. EMPATE')
    elif jog == 'Pedra' and bot == 'Papel':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. O COMPUTADOR VENCEU')
    elif jog == 'Pedra' and bot == 'Tesoura':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. VOCÊ VENCEU')
    elif jog == 'Papel' and bot == 'Pedra':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. VOCÊ VENCEU')
    elif jog == 'Papel' and bot == 'Tesoura':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. O COMPUTADOR VENCEU')
    elif jog == 'Tesoura' and bot == 'Pedra':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. O COMPUTADOR VENCEU')
    elif jog == 'Tesoura' and bot == 'Papel':
        print(f'Você escolheu {jog} e o computador escolheu {bot}. VOCÊ VENCEU')
    rep = input('Jogar novamente (1) SIM  (2) NÃO :  ')
    if rep == '2':
        break
    
