num = int(input('Informe o valor inicial: '))
razao = int(input('Informe a razão da PA: '))
pa = 0

print(num)
for c in range(0, 9):
    num += razao
    print(num)