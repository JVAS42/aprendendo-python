from random import randint

from Mundo2.exercicio047 import contador

jogo_dado = dict()

for i in range(0, 4):
    valor_dado = randint(1, 6)
    nome_jogador = 'Jogador'+str(i+1)
    print(f'Jogador{i+1} tirou {valor_dado} no dado.')

    jogo_dado[nome_jogador] = valor_dado

jogo_dado_ordenado = dict(sorted(jogo_dado.items(), key=lambda item: item[1], reverse=True))
print(20*'=*')
print('== RANKING DOS JOGADORES ==')

contador = 0
for nome_jogador, valor_dado in jogo_dado_ordenado.items():
    print(f'{contador+1} lugar: {nome_jogador} tirou {valor_dado} no dado')
    contador += 1
