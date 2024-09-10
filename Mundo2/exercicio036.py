valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

valorMensalidade = valorCasa/(anos*12)
valorMinimo = salario*0.3

if valorMensalidade <= valorMinimo:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorCasa, anos, valorMensalidade))
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorCasa, anos, valorMensalidade))
    print('Empréstimo NEGADO!')