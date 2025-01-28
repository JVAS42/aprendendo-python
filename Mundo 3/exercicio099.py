def analisa_maior(* numeros):
    print('Analisando os valores...')
    for i in range(0, len(numeros)):
        if i == 0:
            maior_valor = numeros[i]
        else:
            if maior_valor < numeros[i]:
                maior_valor = numeros[i]
        print(numeros[i], end=' ')
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}')


analisa_maior(2, 9, 4, 5, 7, 1)
