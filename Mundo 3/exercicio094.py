lista_de_cadastro = list()
dados_pessoas = dict()
media_idade = 0
resposta = 'S'

while True:
    if resposta == 'S' or resposta == 'N':
        if resposta == 'N':
            break
        else:
            dados_pessoas['nome'] = str(input('Nome: '))
            while True:
                dados_pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
                if dados_pessoas['sexo'] == 'M' or dados_pessoas['sexo'] == 'F':
                    break
                print('ERRO! Por favor, digite apenas M ou F.', end=' ')
            dados_pessoas['idade'] = int(input('Idade: '))

            lista_de_cadastro.append(dados_pessoas.copy())
    else:
        print('ERRO! Por favor digite apenas S(Sim) ou N(Não)', end=' ')

    resposta = str(input('Quer continuar? [S/N]: ')).upper()


print('=-='*20)
print(f' A) Ao todo temos {len(lista_de_cadastro)} pessoas cadastrada.')

for i in range(0, len(lista_de_cadastro)):
    media_idade += lista_de_cadastro[i]['idade']
media_idade = media_idade/len(lista_de_cadastro)
print(f' B) A média de idade é de {media_idade}')

print(f' C) As mulheres cadastradas foram', end=' ')
for i in range(0, len(lista_de_cadastro)):
    if lista_de_cadastro[i]['sexo'] == 'F':
        print(lista_de_cadastro[i]['nome'], end=' ')
print()

print(f' D) Lista de pessoas que estão acima da média:')
for i in range(0, len(lista_de_cadastro)):
    if lista_de_cadastro[i]['idade'] > media_idade:
        print(f'nome = {lista_de_cadastro[i]["nome"]}; '
              f'sexo = {lista_de_cadastro[i]["sexo"]}; '
              f'idade = {lista_de_cadastro[i]["idade"]}')
