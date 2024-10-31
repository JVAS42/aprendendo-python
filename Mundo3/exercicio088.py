from random import randint

lista_de_jogos = list()
jogos = list()

total_de_jogos = int(input('Informe a quantidade de jogos que você deseja: '))
for gera_jogos in range(0, total_de_jogos):
    for gerador_de_numeros in range(0, 6):
        num = randint(0, 60)
        jogos.append(num)
    lista_de_jogos.append(jogos[:])
    jogos.clear()

for mostra_jogos in range(0, len(lista_de_jogos)):
    print(f'{mostra_jogos+1}º jogo: {lista_de_jogos[mostra_jogos]}')
