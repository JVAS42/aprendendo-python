matriz = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
    ]

somaPares = 0
somaTerceiraColuna = 0
maiorValorsegundaLinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da linha {linha+1} coluna {coluna+1}: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        if (matriz[linha][coluna]) % 2 == 0:
            somaPares += (matriz[linha][coluna])
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maiorValorsegundaLinha = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maiorValorsegundaLinha:
                    maiorValorsegundaLinha = matriz[linha][coluna]

print('MATRIZ')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
    print()

print(f'\nA) Soma de todos os valores pares é {somaPares}')
print(f'B) Soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'C) O maior valor da segunda linha é {maiorValorsegundaLinha}')
