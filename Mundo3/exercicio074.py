import random
from random import randint

numerosAleatorios = tuple(randint(0, 1000) for numeros in range(5))

print(numerosAleatorios)
for mostraNum in range (0, 5):
    if mostraNum == 0:
        menorNum  = numerosAleatorios[mostraNum]
        maiorNum = numerosAleatorios[mostraNum]
    else:
        if numerosAleatorios[mostraNum] < menorNum:
            menorNum = numerosAleatorios[mostraNum]
        if numerosAleatorios[mostraNum] > maiorNum:
            maiorNum = numerosAleatorios[mostraNum]

    print(f'{mostraNum+1}º número da tupla é {numerosAleatorios[mostraNum]}')

print(f'\nO menor número da tupla é {menorNum} e o maior número da tupla é {maiorNum}')
