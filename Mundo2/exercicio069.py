contadorMaiorIdade = 0
contadorHomens = 0
contadorMulheresMaiorIdade = 0

while True:
    resposta = str(input('Você deseja cadastra mais um pessoa? [S/N]: ')).strip().upper()
    if resposta == 'S':
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if idade > 18:
            contadorMaiorIdade += 1

        if sexo == 'M':
            contadorHomens += 1
        elif sexo == 'F':
            if idade > 20:
                contadorMulheresMaiorIdade += 1
        else:
            print('Sexo não encontrado')
    elif resposta == 'N':
        break
    else:
        print('Resposta não encontrada, tente novamente!')

print(f'Tem {contadorMaiorIdade} pessoa maior de idade')
print(f'Tem {contadorHomens} homens cadastrados')
print(f'Tem {contadorMulheresMaiorIdade} maiores de 20 anos')
