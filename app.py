import random

NumeroMaximoDoJogo = 10
NumberSecreto = random.randint(1, NumeroMaximoDoJogo)
QDT = 1

print('Bem vindo ao jogo do numero secreto')
Chute = int(input(f'Chute um numero de 1 ate {NumeroMaximoDoJogo}: '))

while Chute != NumberSecreto:
    if Chute < NumberSecreto:
        print('O numero secreto e maior.')
        Chute = int(input('Fazer outro chute: '))
        QDT += 1
    else:
        print('O numero secreto e menor.')
        Chute = int(input('Fazer outro chute: '))
        QDT += 1
else:
    print(f'Voce acertou o numero secreto: {NumberSecreto}, Voce chutou {QDT} tentativas.')