valores = list()

for i in range (0,5):
    valores.append(int(input(f'Informe o {i+1}º valor: ')))

print(f'O valores digitados foram: {valores}')
print(f'O maior valor digitado é {max(valores)}')
print(f'O menor valor digitado é {min(valores)}')