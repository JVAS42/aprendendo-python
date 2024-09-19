palavraDigitada = str(input('Digite a frase: ')).strip().upper().split()

palavraDigitada = ''.join(palavraDigitada)
inverterPalavra = palavraDigitada[::-1]

if palavraDigitada == inverterPalavra:
    print('O inverso de {} é {}'.format(palavraDigitada, inverterPalavra))
    print('É UM PALÍNDROMO')
else:
    print('O inverso de {} é {}'.format(palavraDigitada, inverterPalavra))
    print('NÃO É PALÍNDROMO')