distancia = float(input('Qual é a distância da sua viagem? '))

print('Você está  prestes a começar uma viagem de {:.2f}km.'.format(distancia))
if distancia > 200:
    valorCorrida = distancia*0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(valorCorrida))
else:
    valorCorrida = distancia*0.5
    print('E o preço da sua passagem será de R${:.2f}'.format(valorCorrida))