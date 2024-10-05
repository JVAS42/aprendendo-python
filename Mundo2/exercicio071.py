print('{:^30}'.format('BANCO'))

valorSacado = int(input('Qual o valor a ser sacado: R$'))
total = valorSacado
notaAtual = 50
totalNotas = 0

while True:
    if total >= notaAtual:
        total = total - notaAtual
        totalNotas = totalNotas + 1
    else:
        totalNotas = 0
        if total != 0:
            print(f'Sacou {totalNotas} nota(s) de R${notaAtual}')
        if notaAtual == 50:
            notaAtual = 20
        elif notaAtual == 20:
            notaAtual = 10
        elif notaAtual == 10:
            notaAtual = 1
        else:
            break
