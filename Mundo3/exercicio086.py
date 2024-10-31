matriz = [[], [], [],
          [], [], [],
          [], [], []]

for i in range(0, 9):
    num = int(input(f'Informe o {i + 1}º valor da matriz: '))
    matriz[i].append(num)

for i in range(0, 9):
    if i%3 == 0:
        print()
    print(matriz[i], end=' ')
