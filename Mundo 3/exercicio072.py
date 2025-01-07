tupla_de_numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                    'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero_escolhido = int(input('Digite um número entre 0 e 20: '))
while True:
    numero_escolhido = int(input('Digite um número entre 0 e 20: '))
    if numero_escolhido > 20:
        print('Número não encontrado. Tente novamente!')
    else:
        print(f'O número informado foi {tupla_de_numeros[numero_escolhido]}')
        break
