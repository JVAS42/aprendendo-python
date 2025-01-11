lista_de_numeros_digitados = list()

while True:
    valor_informado = int(input('Informe um novo valor: '))

    if valor_informado in lista_de_numeros_digitados:
        print('Valor duplicado! Não vou adicionar!')
    else:
        print('Valor adicionado com sucesso!')
        lista_de_numeros_digitados.append(valor_informado)

    continuar = str(input('Digite [S] se deseja continuar: ')).upper()

    if continuar != 'S':
        break

print(f'\nVocê digitou os valor {sorted(lista_de_numeros_digitados)}')
