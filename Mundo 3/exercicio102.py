def fatorial(num, show = False):
    '''
    → Função calcular o fatorial de um número!
    :param num: É número que vai ser calculado o fatorial.
    :param show: (Opcional; Default = False). Se escolher True a função mostra o calculo efetuado.
    :return: O valor do fatorial do num escolhido.
    '''
    resultado = 1
    for i in range(num, 0, -1):
        if show == True:
            if i != 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')
        resultado = resultado * i
    return resultado

help(fatorial)
print(fatorial(5))
print(fatorial(5, show=True))
