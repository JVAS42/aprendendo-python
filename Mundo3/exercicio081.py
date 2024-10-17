listaDeValores = list()

while True:
    valor = int(input('Informe o valor a ser adicionado na lista [-1 Encerra]: '))
    if valor != -1:
        listaDeValores.append(valor)
    else:
        break

#Letra A
print(f'Foram digitados {len(listaDeValores)} valores')

#Letra B
print(f'Decrescente: {sorted(listaDeValores, reverse=True)}')

#Letra C
if 5 in listaDeValores:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não está na lista')
