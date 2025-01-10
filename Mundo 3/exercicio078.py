valores_informados = list()
maior = menor = 0

for i in range(0, 5):
    valores_informados.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = valores_informados[i]
        menor = valores_informados[i]
    else:
        if maior < valores_informados[i]:
            maior = valores_informados[i]
        if menor > valores_informados[i]:
            menor = valores_informados[i]

print(f'Você digitou os valores {valores_informados}')

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i in range(0, len(valores_informados)):
    if maior == valores_informados[i]:
        print(f'{i}', end='... ')

print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for i in range(0, len(valores_informados)):
    if menor == valores_informados[i]:
        print(f'{i}', end='... ')
