num = int(input('Informe o valor inicial: '))
razao = int(input('Informe a razão da PA: '))
cont = 1

while cont <= 10:
    print(num, end=' > ')
    num = num + razao
    cont = cont + 1
print('FIM')
