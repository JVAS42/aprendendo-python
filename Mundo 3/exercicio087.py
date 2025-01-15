import exercicio086
soma_pares = 0
soma_terceira_coluna = 0
maior = 0

print('='*30)

for i in range(0, 3):
    for j in range(0, 3):
        if exercicio086.matriz[i][j] % 2 == 0:
            soma_pares = soma_pares + exercicio086.matriz[i][j]
        if i == 2:
            soma_terceira_coluna = soma_terceira_coluna + exercicio086.matriz[i][j]
        if i == 1:
            if maior < exercicio086.matriz[i][j]:
                maior = exercicio086.matriz[i][j]

print(f'A soma dos pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior}')
