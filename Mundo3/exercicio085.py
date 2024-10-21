listaNumeros = [[], []]

for i in range (0, 7):
    num = int(input(f'Informe o {i+1}º  número: '))
    if num % 2 == 0:
        listaNumeros[0].append(num)
    else:
        listaNumeros[1].append(num)

listaNumeros[0].sort()
listaNumeros[1].sort()
print(f'Pares Cresente: {listaNumeros[0]}')
print(f'Ímpares Cresente: {listaNumeros[1]}')
