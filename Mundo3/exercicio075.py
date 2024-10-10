#numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))
from pprint import pprint

contadorNove = 0
contadorPares = 0

numEmTupla = tuple(int(input(f"igte o {i+1}º número: ")) for i in range(4))
for i in range (4):
    if numEmTupla[i] == 9:
        contadorNove += 1
    if numEmTupla[i] == 3:
        print(f'A posição do primeiro número 3 na tupla é {numEmTupla[i]}')
    if numEmTupla[i]%2 == 0:
        contadorPares += 1

print(f'Foram digitados {contadorNove} números nove')
print(f'Foram digitadis {contadorPares} números pares')
