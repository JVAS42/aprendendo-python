tupla = ('Lápis', 1.75, 'Caderno', 10.50, 'Caneta', 2.5, 'Folha', 0.25, 'Borracha', 2.00)

for pos in range(0, len(tupla)):
    if pos%2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]}')