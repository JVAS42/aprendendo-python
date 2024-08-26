valorReal = float(input('Quanto dinheiro você tem na carteira? R$'))
valorDolar = valorReal/5.49

print('Com R${:.2f} você pode comprar US${:.2f}'.format(valorReal, valorDolar))