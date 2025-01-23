estatistica_jogador = dict()
quantidade_gols = list()
total_de_gols = 0

estatistica_jogador['nome'] = str(input('Nome do jogador: '))
quantidade_partida = int(input(f'Quantas partidas {estatistica_jogador["nome"]} jogou? '))
if quantidade_partida >= 1:
    for i in range(0, quantidade_partida):
        quantidade_gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
        total_de_gols += quantidade_gols[i]
    estatistica_jogador['gols'] = quantidade_gols[:]
    estatistica_jogador['total'] = total_de_gols

print('*=*=*'*5)
print(estatistica_jogador)
print('*=*=*'*5)
for k, v in estatistica_jogador.items():
    print(f'Campo {k} tem o valor {v}')
print('*=*=*'*5)
print(f'O jogador {estatistica_jogador["nome"]} jogou {len(estatistica_jogador["gols"])} partidas')
for i in range(0, len(estatistica_jogador['gols'])):
    print(f' => Na {i+1}º partida, {estatistica_jogador["nome"]} fez {estatistica_jogador["gols"][i]} gols.')
