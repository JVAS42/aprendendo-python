somaNumPares = 0
contadorDeNum = 0

for c in range(1, 7):
    num = int(input('Informe um número: '))
    if (num % 2 == 0):
        contadorDeNum += 1
        somaNumPares += c

print('Você informou {} números pares e a soma é {}'.format(contadorDeNum, somaNumPares))
