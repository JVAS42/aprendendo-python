listaCompleta = list()
listaPares = list()
listaImpares = list()

while True:
    valor = int(input('Informe um valor: '))
    if valor in listaCompleta:
        break
    else:
        listaCompleta.append(valor)

for i in range(len(listaCompleta)):
    if listaCompleta[i] % 2 == 0:
        listaPares.append(listaCompleta[i])
    else:
        listaImpares.append(listaCompleta[i])

print(f'Lista completa: {listaCompleta}\nLista apenas dos pares: {listaPares}\nLista apenas dos impares: {listaImpares}')