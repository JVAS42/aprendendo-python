from random import randint

listaDeJogadas = ['PEDRA', 'PAPEL', 'TESOURA']
contadorDeVitorias = 0

while True:
    jogadaComputador = (listaDeJogadas[randint(0, 2)])
    jogada = str(input('Informe sua jogada [PEDRA, PAPEL, TESOURA]: ')).strip().upper()
    if jogada == 'PEDRA':
        if jogadaComputador == 'PEDRA':
            print('Empatou, vamos tenta novamente!')
        elif jogadaComputador == 'PAPEL':
            print('Você perdeu!')
            break
        else:
            print('Você ganhou')
            contadorDeVitorias += 1
    elif jogada == 'PAPEL':
        if jogadaComputador == 'PEDRA':
            print('Você ganhou')
            contadorDeVitorias += 1
        elif jogadaComputador == 'PAPEL':
            print('Empatou, vamos tenta novamente!')
        else:
            print('Você perdeu!')
            break
    elif jogada == 'TESOURA':
        if jogadaComputador == 'PEDRA':
            print('Você perdeu!')
            break
        elif jogadaComputador == 'PAPEL':
            print('Você ganhou')
            contadorDeVitorias += 1
        else:
            print('Empatou, vamos tenta novamente!')
    else:
        print('Jogada não encontrada, tente novamente')

print(f'Você ganhou {contadorDeVitorias} vezes')
