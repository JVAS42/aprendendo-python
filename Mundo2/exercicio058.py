from random import randint

print('Vou penser em um número entre 0 e 10. Tente adivinhar...')
numMaquina = randint(0,10)
numEscolha = -1
quantPalpites = 0

while numMaquina != numEscolha:
    numEscolha = int(input('Em que número eu pensei? '))
    if numMaquina == numEscolha:
        print('PARABÉNS! Você me venceu!')
    else:
        print('Você não acertou o número, tente novamente!')

    quantPalpites+=1
print('Você tentou {} vezes até acertar!'.format(quantPalpites))
