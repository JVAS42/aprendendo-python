'''
Tive um pouco de dificuldade, pq eu queria resolver usando lista e tuplas,
mas pela resolução do vídeo, ele resolve usando apenas uma lista
'''

from random import randint

jogo_do_dado = dict()
lista_de_jogos = list()

for i in range(1, 5):
    jogo_do_dado['nome'] = 'jogador' + str(i)
    jogo_do_dado['dado'] = randint(1, 6)
    print(f'{jogo_do_dado["nome"]} tirou {jogo_do_dado["dado"]} no dado.')
    lista_de_jogos.append(jogo_do_dado.copy())

ranking = sorted(lista_de_jogos, key=lambda x: x['dado'], reverse=True)
print('-=-'*20)
print('== RANKING DOS JOGADORES ==')

for i in range(0, len(ranking)):
    print(f'{i+1}º lugar: {ranking[i]["nome"]} com {ranking[i]["dado"]}')
