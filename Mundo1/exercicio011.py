largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
dimensao = largura*altura
print('Sua parede tem a dimensão de {:.1f} x {:.1f} e sua área é de {:.3f}m'.format(largura, altura, dimensao))
litrosDeTinta = dimensao/2
print('Para pintar essa parede, você precisa de {} litros de tinta'.format(litrosDeTinta))