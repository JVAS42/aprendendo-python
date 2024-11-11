aluno = dict()

aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = float(input('Informe a média do aluno: '))

print(20*'=-=')
print(f'Nome do aluno {aluno["nome"]}')
print(f'A média do aluno é {aluno["media"]}')
if aluno['media'] >= 7.0:
    print(f'{aluno["nome"]} foi aprovado por média')
elif aluno['media'] < 7.0 and aluno['media'] >= 5.0:
    print(f'{aluno["nome"]} está em recupeção')
else:
    print(f'{aluno["nome"]} foi reprovado')
print(20*'=-=')
