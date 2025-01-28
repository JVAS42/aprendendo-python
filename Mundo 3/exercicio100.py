from random import randint

soma_pares = 0

def gera_vetor():
    lst = []
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        print(num, end=' ')
        lst.append(num)
    print('PRONTO!')
    return lst

def verifica_par(lista_numeros):
    global soma_pares
    #lista_numeros = gera_vetor()
    for i in range(0, len(lista_numeros)):
        if lista_numeros[i] % 2 == 0:
            soma_pares += lista_numeros[i]
    print(f'Somando os valores pares de {lista_numeros}, temos a soma = {soma_pares}')


verifica_par(gera_vetor())
