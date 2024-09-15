from datetime import datetime

ano = int(input(''))
idade = datetime.now().year - ano

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação MIRIN')
#O if podia ser if idade <= 14 por conta do elif
elif idade > 9 and idade <= 14:
    print('Classificação INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
