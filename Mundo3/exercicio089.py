boletin = list()
nome_notas = list()

while True:
    check = str(input('Digite N se deseja encerrar: ')).strip().upper()
    if check == 'N':
        break
    nome_notas.append(str(input('Nome: ')))
    nome_notas.append(float(input('Informe a primeira nota : ')))
    nome_notas.append(float(input('Informe a segunda nota : ')))
    boletin.append(nome_notas[:])
    nome_notas.clear()

soma = 0
print('=*BOLETIN*=')
for i in range(0, len(boletin)):
    for j in range(0, 3):
        if j == 0:
            print(f'| ALUNO: {boletin[i][j]} | ', end=' ')
        if j > 0:
            soma += boletin[i][j]
        if j == 2:
            print(f'MÉDIA:{soma/2} |')
            soma = 0

print()
while True:
    check = str(input('Digite N se deseja encerrar: ')).strip().upper()
    if check == 'N':
        break
    nota_aluno = int(input(f'Escolhar um numero de 0 até {len(boletin)-1}: '))
    print(boletin[nota_aluno])

    '''
        for i in range(0, len(boletin)):
        for j in range(0, 3):
            if j == 0:
                print(f'| ALUNO: {boletin[i][j]} | ', end=' ')
            if j == 1:
                print(f'| NOTA 1: {boletin[i][j]} | ', end=' ')
            if j == 2:
                print(f'| NOTA 2: {boletin[i][j]} | ')
    '''
