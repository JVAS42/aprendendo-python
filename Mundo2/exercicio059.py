escolha = 0
num1 = float(input('Informe o primeiro valor: '))
num2 = float(input('Informe o segundo valor: '))

while escolha != 5:

    print('='*5+' MENU '+'='*5)
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair')
    escolha = int(input('SUA ESCOLHA: '))

    if escolha == 1:
        print('{} + {} = {}'.format(num1, num2, num1+num2))
    elif escolha == 2:
        print('{} * {} = {}'.format(num1, num2, num1*num2))
    elif escolha == 3:
        if num1 > num2:
            print('Número 1 escolhido é o maior ele é {}'.format(num1))
        elif num2 > num1:
            print('Número 2 escolhido é o maior ele é {}'.format(num2))
        else:
            print('Os números são iguais')
    elif escolha == 4:
        print('Informe novos números')
        num1 = float(input('Informe o primeiro valor: '))
        num2 = float(input('Informe o segundo valor: '))
    elif escolha == 5:
        print('Saindo...')
    else:
        print('Valor não encontrado')
