contador = 0

while contador < 1:
    sexo = str(input('Informe o seco [M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        contador = contador + 1
        if sexo == 'M':
            print('Você é do sexo masculino')
        else:
            print('Você é do sexo femino')

    else:
        print('Sexo inváivo, tente novamente')
        