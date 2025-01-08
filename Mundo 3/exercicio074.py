from random import randint

tupla_de_numeros = tuple(randint(1, 10) for gerador_de_numeros in range(0, 5))

print('Os valores sorteados foram:', end=' ')
for mostrar_numeros in tupla_de_numeros:
    print(mostrar_numeros, end=' ')

for posicao_numeros in range(0, len(tupla_de_numeros)):
    if posicao_numeros != 0:
        if menor_valor > tupla_de_numeros[posicao_numeros]:
            menor_valor = tupla_de_numeros[posicao_numeros]
        if maior_valor < tupla_de_numeros[posicao_numeros]:
            maior_valor = tupla_de_numeros[posicao_numeros]
    else:
        menor_valor = tupla_de_numeros[posicao_numeros]
        maior_valor = tupla_de_numeros[posicao_numeros]

print()
print(f'O maior valor sorteado foi {maior_valor}')
print(f'O menor valor sorteado foi {menor_valor}')

'''
Eh possivel colocar tudo dentro de um FOR, mas por questao de praticar tipos de FOR eu escolhi fazer dois FOR
'''
