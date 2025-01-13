lista_de_numeros = [[], []]

for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor%2 == 0:
        lista_de_numeros[0].append(valor)
    else:
        lista_de_numeros[1].append(valor)

lista_de_numeros[0].sort()
lista_de_numeros[1].sort()
print(f'Os valores pares digitados foram: {lista_de_numeros[0]}')
print(f'Os valores ímpares digitados foram: {lista_de_numeros[1]}')
