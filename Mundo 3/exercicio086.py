matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        valor_matriz = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(valor_matriz)

print('='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
