tupla_de_produtos = ('Lápis', 1.75,
                     'Borracha', 2.00,
                     'Caderno', 15.90,
                     'Estojo', 25.00,
                     'Transferidor', 4.20,
                     'Compasso', 9.99,
                     'Mochila', 120.32,
                     'Canetas', 22.30,
                     'Livro', 34.90)

print('_'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('_'*40)

for i in range(0, len(tupla_de_produtos), 2):
    print(f'{tupla_de_produtos[i]} {"."*20:^20} R${tupla_de_produtos[i+1]:.2f}')
