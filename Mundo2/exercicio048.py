somaNumImpares = 0

for numeros in range(1, 501):
    if (numeros % 2 != 0):
        if (numeros % 3 == 0):
            somaNumImpares += numeros
print(somaNumImpares)