num = int(input('Informe o número que você deseja saber a tabuada: '))

for multiplica in range(1, 11):
    print('{} x {} = {}'.format(num, multiplica, num*multiplica))