palavras = ('Concole', 'Playstation', 'Xbox', 'Computador',
            'Controle', 'Mouse', 'Teclado', 'Monitor')

for p in palavras:
    print(f'Na palavra {p.upper()} têm as vogais', end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
