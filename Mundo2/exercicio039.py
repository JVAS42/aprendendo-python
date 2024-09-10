from datetime import datetime

ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, datetime.now().year))

if idade > 18:
    print('Você se alist  ou há {} anos'.format(idade-18))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
else:
    print('Você deve se alistar IMEDIATAMENTE')
