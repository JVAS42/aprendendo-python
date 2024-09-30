totalGasto = 0
contProdutoMil = 0

nomeProduto = str(input('Nome do produtor: ')).strip().upper()
produtoMaisBarato = nomeProduto
valorProduto = float(input('Valor do produtor: R$'))
valorProdutoMaisBarato = valorProduto
if valorProduto >= 1000:
    contProdutoMil += 1
totalGasto += valorProduto

while True:
    resposta = str(input('Deseja continuar a compra? [S/N]: ')).strip().upper()
    if resposta == 'S':
        nomeProduto = str(input('Nome do produtor: ')).strip().upper()
        valorProduto = float(input('Valor do produtor: R$'))
        if valorProduto >= 1000:
            contProdutoMil += 1
        if valorProduto < valorProdutoMaisBarato:
            produtoMaisBarato = nomeProduto
        totalGasto += valorProduto
    elif resposta == 'N':
        break
    else:
        print('Reposta não encontrada')

print(f'Total gasto = R${totalGasto:.2f}')
print(f'Totla de produtos com valor maior que R$1000 é {contProdutoMil}')
print(f'O produto mais barato é o {produtoMaisBarato.capitalize()}')
