listaValores = list()

while True:
    valor = int(input('Informe um número: '))

    if valor in listaValores:
        break
    else:
        listaValores.append(valor)

print(f'Os valores digitados foram {listaValores}')
print(f'Em ordem crescente {sorted(listaValores)}')