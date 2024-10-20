listaDeNumeros = list()

for i in range (0, 5):
    listaDeNumeros.append(int(input(f'Informe o {i + 1}º valor: ')))

print(listaDeNumeros)

compara = 0
for i in range (0, len(listaDeNumeros)):
    compara = i + 1
    while compara < 5:
        if listaDeNumeros[i] > listaDeNumeros[compara]:
            listaDeNumeros[i], listaDeNumeros[compara] = listaDeNumeros[compara], listaDeNumeros[i]

        compara += 1
print(listaDeNumeros)
