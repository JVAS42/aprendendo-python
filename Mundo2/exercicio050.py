somaNumPares = 0

for c in range(1, 7):
    num = int(input('Informe um número: '))
    if (num % 2 == 0):
        somaNumPares += c

print('Soma dos números pares = {}'.format(somaNumPares))