lista_numeros = list()
lista_numeros_pares = list()
lista_numeros_impares = list()

while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Digite [S] se deseja continuar: ')).upper()
    if continuar != 'S':
        break

print(f'A lista completa é {lista_numeros}')

for i in range(0, len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        lista_numeros_pares.append(lista_numeros[i])
    else:
        lista_numeros_impares.append(lista_numeros[i])

print(f'A lista de pares é {lista_numeros_pares}')
print(f'A lista de ímpares é {lista_numeros_impares}')
