num = int(input('Informe o valor inicial: '))
razao = int(input('Informe a razão da PA: '))
mostrarMais = 10
total = 0
cont = 1

while mostrarMais != 0:
    total = total + mostrarMais
    while cont <= total:
        print(num, end=' > ')
        num = num + razao
        cont = cont + 1
    print('PAUSA')
    mostrarMais = int(input('Quantos termo você quer mostrar a mais? '))
print('FIM')
print('O total de termos mostrado foi de {}'.format(cont))
