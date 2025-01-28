def contador(valor_inicial, valor_final, intervalo):
    print('~'*30)
    print(f'Contagem de {valor_inicial} até {valor_final} de {intervalo} em {intervalo}')
    while valor_inicial != valor_final:
        print(valor_inicial, end=' ')
        valor_inicial += intervalo

    print(valor_inicial, end=' ')
    print('FIM!')
    print('~' * 30)


contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
valor_inicial = int(input('Início: '))
valor_final = int(input('Fim: '))
intervalo = int(input('Passo: '))
contador(valor_inicial, valor_final, intervalo)
