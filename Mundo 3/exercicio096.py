def area(l, c):
    a = l*c
    return a


print('Controle de Terretos')
l = float(input('Largura (M): '))
c = float(input('Comprimento (M): '))
print(f'A área de um terreno {l}m x {c}m é de {area(l, c)}m')
