from random import randint

print('Vou penser em um número entre 0 e 5. Tente adivinhar...')
numMaquina = randint(0,5)
numEscolha = int(input('Em que número eu pensei? '))
print('PROCESSANDO')
if numEscolha == numMaquina:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numMaquina, numEscolha))