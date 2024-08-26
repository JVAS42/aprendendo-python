valorEmMetros = int(input('Uma distância em metros: '))

print('A medida de {:.1f} corresponde a\n'.format(valorEmMetros))
print('{:.3f}km\n{:.2f}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(valorEmMetros/1000, valorEmMetros/100, valorEmMetros/10, valorEmMetros*10, valorEmMetros*100, valorEmMetros*1000))