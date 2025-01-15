from random import random, randint

print('JOGO NA MEGA SENA')
print('='*18)

quant_numeros = 6
lista_de_jogos = list()
numeros_jogo = list()
num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, num_jogos):
    while True:
        numero = randint(1, 61)
        if numero not in numeros_jogo:
            numeros_jogo.append(numero)
            quant_numeros = quant_numeros - 1
        if quant_numeros == 0:
            break

    quant_numeros = 6
    numeros_jogo.sort()
    lista_de_jogos.append(numeros_jogo[:])
    numeros_jogo.clear()

for i in range(0, len(lista_de_jogos)):
    print(f'Jogo {i}: {lista_de_jogos[i]}')
# print(lista_de_jogos)
