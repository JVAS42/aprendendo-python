lista_com_numeros_ordenados = list()

for i in range(0, 5):
    numero_informado = int(input('Digite um valor: '))

    if i == 0:
        lista_com_numeros_ordenados.append(numero_informado)
        print('Adicionado no final da lista...')
    else:
        for j in range(0, len(lista_com_numeros_ordenados)):
            if numero_informado < lista_com_numeros_ordenados[j]:
                lista_com_numeros_ordenados.insert(j, numero_informado)
                print(f'Adicionador na posição {j} da lista')
                break
        if numero_informado > lista_com_numeros_ordenados[len(lista_com_numeros_ordenados)-1]:
            lista_com_numeros_ordenados.append(numero_informado)
            print('Adicionado no final da lista...')

print(f'\nO valores digitados em ordem fora {lista_com_numeros_ordenados}')
