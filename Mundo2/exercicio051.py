num = int(input('Informe o valor inicial: '))
razao = int(input('Informe a razão da PA: '))
pa = 0
decimo = num + (10-1) * razao

print('='*20+'\nTERMOS DE UMA PA\n'+'='*20)
for c in range(num, decimo + razao, razao):
    print(c, end= ' -> ')
print('Fim da PA')
