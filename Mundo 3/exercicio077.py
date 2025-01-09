tupla_de_palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
                     'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
                     'PROGRAMADOR', 'FUTURO')
vogais = "AEIOU"

for i in range(0, len(tupla_de_palavras)):
    palavra_analisada = tupla_de_palavras[i]
    vogais_encontradas = [letra for letra in palavra_analisada if letra in vogais]
    print(f'Na palavra {tupla_de_palavras[i]} temos {" ".join(vogais_encontradas).lower()}')
