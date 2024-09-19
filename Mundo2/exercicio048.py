somaNumImpares = 0
contadorNumImpares = 0

for numeros in range(1, 501):
    if (numeros % 2 != 0):
        if (numeros % 3 == 0):
            contadorNumImpares += 1
            somaNumImpares += numeros
print('A soma de todos os {} valores é {}'.format(contadorNumImpares, somaNumImpares))
