somaIdade = 0
idadeMaisVelho = 0
contMulherMenor = 0

for c in range (1, 5):
    print('-'*5+' {}° PESSOA '.format(c)+'-'*5)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if idade > idadeMaisVelho and sexo == 'M':
        idadeMaisVelho = idade
        nomeMaisVelho = nome

    if idade <= 20 and sexo == 'F':
        contMulherMenor += 1

    somaIdade += idade

print('A média de idade do grupo é de {:.1f} anos'.format(somaIdade/4))
print('O homem mais velhor tem {} anos e se chama {}'.format(idadeMaisVelho, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contMulherMenor))
