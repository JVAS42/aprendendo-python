contador_par = 0

tupla_de_numeros_digitados = tuple(int(input('Digite o número: ')) for numero_digitados in range(0, 4))

for i in range(0, len(tupla_de_numeros_digitados)):
    if tupla_de_numeros_digitados[i] % 2 == 0:
        contador_par += 1

print('Você digitou os valores', tupla_de_numeros_digitados)
print(f'O valor 9 apareceu {tupla_de_numeros_digitados.count(9)} vez(es)')
print(f'O valor 3 apareceu na {tupla_de_numeros_digitados.index(3)+1}º posição')
print(f'Os valores pares digitador foram {contador_par}')
