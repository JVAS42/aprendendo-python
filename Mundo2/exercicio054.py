from datetime import datetime

anoAtual = datetime.now().year
maiorDeIdade = 0
menorDeIdade = 0

for numPessoas in range(1, 8):
    anoNascimento = int(input('Em que ano a {}° pessoas nasceu? '.format(numPessoas)))
    if anoAtual - anoNascimento >= 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1

print('Temos {} pessoas maior de idade'.format(maiorDeIdade))
print('Temos {} pessoas menor de idade'.format(menorDeIdade))
