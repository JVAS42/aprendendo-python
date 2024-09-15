print('='*10 + ' LOJINHA ' + '='*10)
preco = float(input('Preço da comprar: R$'))
print('FORMAS DE PAGAMENTO'+
      '[ 1 ] à vista com dinheiro/pix'+
      '[ 2 ] à vista cartão'+
      '[ 3 ] 2x no cartão'+
      '[ 4 ] 3x ou mais no cartã')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Pagamento em dinheiro ou pix o valor R${:.2f} passa para {:.2f}'.format(preco, preco*0.9))
elif opcao == 2:
    print('Pagamento à vista no cartão o valor R${:.2f} passa para {:.2f}'.format(preco, preco*0.95))
elif opcao == 3:
    print('O valor da comprar é R${:.2f} e foi parcelado em 2x'.format(preco))
    print('Ficou 2 parcelas de R${:.2f}'.format(preco/2))
elif opcao == 4:
    parcela = int(input('Informa a quantidade das parcelas: '))
    print('O valor da comprar é R${:.2f} e foi parcelado em {}'.format(preco, parcela))
    print('Ficou {} parcelas de R${:.2f}'.format(parcela, preco / parcela))
else:
    print('Opção não encontrada')