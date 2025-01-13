lista_nome_peso = list()
lista_dados_temporios = list()
pessoas_pessadas = list()
pessoas_maneiras = list()
maior_peso = menor_peso = total_de_pessoas = 0

while True:
    lista_dados_temporios.append(str(input('Nome: ')))
    lista_dados_temporios.append(float(input('Peso: ')))
    lista_nome_peso.append(lista_dados_temporios[:])

    if total_de_pessoas == 0:
        maior_peso = menor_peso = lista_dados_temporios[1]
        pessoas_pessadas.append(lista_dados_temporios[0])
        pessoas_maneiras.append(lista_dados_temporios[0])
    else:
        if maior_peso < lista_dados_temporios[1]:
            pessoas_pessadas.clear()
            maior_peso = lista_dados_temporios[1]
            pessoas_pessadas.append(lista_dados_temporios[0])
        elif maior_peso == lista_dados_temporios[1]:
            pessoas_pessadas.append(lista_dados_temporios[0])

        if menor_peso > lista_dados_temporios[1]:
            pessoas_maneiras.clear()
            menor_peso = lista_dados_temporios[1]
            pessoas_maneiras.append(lista_dados_temporios[0])
        elif menor_peso == lista_dados_temporios[1]:
            pessoas_maneiras.append(lista_dados_temporios[0])

    total_de_pessoas += 1
    lista_dados_temporios.clear()

    resposta = str(input('Quer continuar? Digite [S]: ')).upper()
    if resposta != 'S':
        break

print(f'Ao todo, você cadastrou {total_de_pessoas} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de {pessoas_pessadas}')
print(f'O menor peso foi de {menor_peso:.1f}Kg. Peso de {pessoas_maneiras}')
