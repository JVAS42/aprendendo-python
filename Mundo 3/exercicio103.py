def ficha_jogador(nome = '<desconhecido>', quant_gols = 0):
    print(f'O jogador {nome} fez {quant_gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha_jogador(quant_gols=gols)
else:
    ficha_jogador(nome, gols)
