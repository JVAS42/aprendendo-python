contadorDeNumeros = 0
soma = 0

while True:
    num = int(input('Informe um número [DIGITE 999 PARA PARAR]: '))
    if num == 999:
        break
    soma += num
    contadorDeNumeros += 1

print(f'Você {contadorDeNumeros} números e soma entre ele é {soma}')
