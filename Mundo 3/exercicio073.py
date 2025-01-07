'''
Exercicio feito em 2024
Eu troquei Chapecoense por Fortaleza, porque sou do nordeste
'''

tabela_brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
                      'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

# A) Os 5 primeiros
print(f'Os cinco primeiros colocados são {tabela_brasileirao[:5]}')

# B) Os últimos 4 colocados
print(f'Os últimos 4 colocados são {tabela_brasileirao[-4:]}')

# C) Times em ordem alfabéticas
print(f'Time em ordem alfabética {sorted(tabela_brasileirao)}')

# D) Posição do Fortaleza
print(f'A posição do Fortaleza é {tabela_brasileirao.index('Fortaleza')+1}º lugar')