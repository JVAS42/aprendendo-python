boletin = dict()

boletin['nome'] = str(input('Nome: '))
boletin['media'] = float(input('Média: '))

if boletin['media'] >= 7:
    boletin['situacao'] = 'Aprovado'
elif boletin['media'] < 7 and boletin['media'] >= 5:
    boletin['situacao'] = 'Recuperação'
else:
    boletin['situacao'] = 'Reprovado'

for k, v in boletin.items():
    print(f'{k} é {v}')