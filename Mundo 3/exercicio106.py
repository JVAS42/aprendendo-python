import exercicio097

def ajuda():
    informa = str(input('Função ou Biblioteca → '))
    while True:
        if informa == 'fim':
            break
        exercicio097.escreva(f'Acessando o manual de comando "{informa}"')
        help(informa)
        informa = str(input('Função ou Biblioteca → '))


ajuda()
