cont = 0
num = 0
soma = 0

while num != 999:
    num = int(input('Informe um número: '))
    soma += num
    cont += 1

print('Você digitou {} números\nE a soma entre eles é de {}'.format(cont, soma-999))