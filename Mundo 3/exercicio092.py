from datetime import datetime

clt = dict()

clt['nome'] = str(input('Nome: '))
ano_de_nascimeto = int(input('Ano de nascimento: '))
clt['idade'] = datetime.now().year - ano_de_nascimeto
clt['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if clt['ctps'] != 0:
    clt['contratação'] = int(input('Ano da contratação: '))
    clt['salario'] = float(input('salário: R$'))
    clt['aposentadoria'] = clt['idade'] + ((clt['contratação'] + 35) - datetime.now().year)

    for k, v in clt.items():
        print(f'{k} é {v}')

else:
    for k, v in clt.items():
        print(f'{k} é {v}')