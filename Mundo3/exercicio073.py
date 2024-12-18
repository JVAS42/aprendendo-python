# Minha Resolução
listaDeTimes = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo',
                'Internacional', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atlético-MG',
                'Grêmio', 'Criciúma', 'Bragantino', 'Juventude', 'Athletico-PR',
                'Fluminense', 'EC Vitória', 'Corithians', 'Cuiabá', 'Atlético-GO')

# Letra A
for i in range (0, 5):
    print(f'{i+1}º {listaDeTimes[i]}')
print(listaDeTimes[:5])
print('\n')

#Letra B
for i in range (16, 20):
    print(f'{i+1}º {listaDeTimes[i]}')
print(listaDeTimes[16:])
print('\n')

#Letra C
tuplaOrdem = sorted(listaDeTimes)
for i in range (0, 20):
    print(f'{tuplaOrdem[i]}')
print(tuplaOrdem)
print('\n')

#Letra D
for i in range (0, 20):
    if listaDeTimes[i] == 'Criciúma':
        print(f'Posição do {listaDeTimes[i]} na tabela é {i+1}º')

# Resolução Curso em Vídeo
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
                'São Paulo', 'Corithians', 'Bahia', 'Cruzeiro', 'Vasco',
                'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
                'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'Os primeiros times: {times[0:5]}')
print(f'Os 4 últimos times: {times[-4:]}')
print(f'Times em ordem algabética: {sorted(times)}')
# Chapeco não está mais na série A
