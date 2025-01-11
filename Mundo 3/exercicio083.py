lista_de_letras = list(str(input('Digite a espressão: ')))
lista_abrindo = list()
lista_fechando = list()

# print(lista_de_letras)

for i in range(0, len(lista_de_letras)):
    if lista_de_letras[i] == '(':
        lista_abrindo.append(lista_de_letras[i])
    if lista_de_letras[i] == ')':
        lista_fechando.append(lista_de_letras[i])

if len(lista_abrindo) == len(lista_fechando):
    print('Sua expressão é válida!')
else:
     print('Sua expressão é inválida!')
