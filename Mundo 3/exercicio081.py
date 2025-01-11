lista_numeros_informado = list()

while True:
    lista_numeros_informado.append(int(input('Digite um valor: ')))
    continuar = str(input('Digite [S] se deseja continuar: ')).upper()
    if continuar != 'S':
        break

lista_numeros_decrescente = sorted(lista_numeros_informado, reverse=True)

print('-='*50)
print(f'Você digitou {len(lista_numeros_informado)} elementos.')
print(f'Os valores em ordem decrescente são {lista_numeros_decrescente}')
if 5 in lista_numeros_informado:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
