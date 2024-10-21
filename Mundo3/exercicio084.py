listaDePessoas = list()
dados = list()
quantPessoas = maisLeve = maisPesada = 0

while True:
    check = str(input('Deseja cadastrar mais uma pessoa [S|N]: ')).strip().upper()
    if check == 'N':
        break
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    listaDePessoas.append(dados[:])
    if quantPessoas == 0:
        maisLeve = dados[1]
        maisPesada = dados[1]
    else:
        if dados[1] < maisLeve:
            maisLeve = dados[1]
        if dados [1] > maisPesada:
            maisPesada = dados[1]
    quantPessoas += 1
    dados.clear()

print(f'Pessoas cadastradas {listaDePessoas}')
print(f'Foram cadastrados {quantPessoas} pessoas.')
print(f'Pessos com mais de {maisPesada}KG da lista:', end=' ')
for i in listaDePessoas:
    if i[1] >= maisPesada:
        print(f'{i[0]}', end=' ')
print(f'Pessos com menos de {maisLeve}KG da lista:', end=' ')
print()
for i in listaDePessoas:
    if i[1] <= maisLeve:
        print(f'{i[0]}', end=' ')
