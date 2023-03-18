print('********************************')
print('Bem vindo ao jogo da forca')
print('********************************')

import random

opcoes4 = ['casa', 'dado', 'teto', 'pata', 'amor', 'tela', 'lata']
opcoes5 = ['cinco', 'outro', 'quina', 'rolha', 'pasta', 'poste', 'carro', 'telha']
opcoes6 = ['pessoa', 'orelha', 'trilho','mastro', 'jantar', 'almoço', 'sapato', 'janela']
opcoes7 = ['janeiro', 'romance', 'estrada', 'teclado', 'primata', 'coraçao', 'gabriel', 'bermuda']
opcoes8 = ['flamengo', 'salvador', 'namorado', 'trabalho', 'cacetete', 'paralelo', 'horrivel', ]

letras_descobertas = []

rep = '1'
erro = False
tentativa = 0

while rep == '1' :
    print('4 - Muito fácil; 5 - Fácil; 6 - Médio; 7 - Difícil; 8 - Muito difícil:  ')
    op = input('Digite a Quantidade de letras que a próxima palavra oculta terá.  (entre 4 e 8):  ')
    if op == '4':
        palavra = random.choice(opcoes4)
    if op == '5':
        palavra = random.choice(opcoes5)
    if op == '6':
        palavra = random.choice(opcoes6)
    if op == '7':
        palavra = random.choice(opcoes7)
    if op == '8':
        palavra = random.choice(opcoes8)
    
    tentativa = 0
    letras_descobertas = []
   

    palavra = list(palavra)

    for i in range(0, len(palavra)):
        letras_descobertas.append('-')

    acertou = False

    while acertou == False:
        letra = str(input('Digite a próxima letra: '))
    

        for i in range(0, len(palavra)):
            if letra == palavra[i]:
                letras_descobertas[i] = letra
            print(letras_descobertas[i])
                 
        acertou = True
        

        for x in range(0, len(letras_descobertas)):

            if letras_descobertas [x] == '-':
                acertou = False
        

        for i in palavra[i]:
            if letra not in palavra:
                tentativa = tentativa + 1 
                print(f'Você ja errou {tentativa} vezes. ')
            if tentativa == int(5):
                print('Game Over')
                rep1 = input('Jogar Novamente (S/N)')
                if rep1 == 's' or rep1 == 'S':
                    acertou = True
                elif rep1 == 'n' or rep1 == 'N':
                    rep = '0'
                    break
                else: 
                    acertou = True
            