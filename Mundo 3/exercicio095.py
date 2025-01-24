lista_de_jogadores = list()  # Para salvar todos os dados informados
estatistica_jogador = dict()  # Para pegar os dados de cada jogador
quantidade_gols = list()  # Lista para salvar os gols
total_de_gols = 0
resposta = 'S'

while True:
    if resposta == 'S' or resposta == 'N':
        if resposta == 'N':
            break
        else:
            estatistica_jogador['nome'] = str(input('Nome do jogador: '))
            quantidade_partida = int(input(f'Quantas partidas {estatistica_jogador["nome"]} jogou? '))
            if quantidade_partida >= 1:
                for i in range(0, quantidade_partida):
                    quantidade_gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
                    total_de_gols += quantidade_gols[i]
                estatistica_jogador['gols'] = quantidade_gols[:]
                estatistica_jogador['total'] = total_de_gols
                lista_de_jogadores.append(estatistica_jogador.copy())
                quantidade_gols.clear()
                total_de_gols = 0
    else:
        print('ERRO! Por favor digite apenas S(Sim) ou N(Não)', end=' ')

    resposta = str(input('Quer continuar? [S/N]: ')).upper()

print('-=-'*20)
# Dps vou pesquisar de como fazer um print TABULAR em python
print('COD  |   NOME    |   GOLS    |   TOTAL GOLS  |')
print('---'*20)
for i in range(0, len(lista_de_jogadores)):
    print(f'{i}     |   {lista_de_jogadores[i]["nome"]}     |   {lista_de_jogadores[i]["gols"]}     |   {lista_de_jogadores[i]["total"]}    |')
print('---'*20)
while True:
    resposta = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if resposta == 999:
        break
    else:
        print(f'LEVATAMENTO DO JOGADOR {lista_de_jogadores[resposta]['nome']}')
        for i in range(0, len(lista_de_jogadores[resposta]['gols'])):
            print(f'No jogo {i+1}, {lista_de_jogadores[resposta]["nome"]} fez {lista_de_jogadores[resposta]["gols"][i]}')
