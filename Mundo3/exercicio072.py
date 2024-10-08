tuplasDeNumeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                   'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numEscolhido = int(input('Informe um número: '))
    if numEscolhido >= 0 and numEscolhido <= 20:
        print(f'Número escolhido foi {tuplasDeNumeros[numEscolhido]}')
    else:
        print('Número informado não foi encontrado')
        break