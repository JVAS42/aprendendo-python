boletin = list()
dados_alunos = list()

while True:
    dados_alunos.append(str(input('Nome: ')))
    dados_alunos.append(float(input('Nota 1: ')))
    dados_alunos.append(float(input('Nota 2: ')))
    boletin.append(dados_alunos[:])

    dados_alunos.clear()
    resposta = str(input('Quer continuar? [S]: ')).upper()
    if resposta != 'S':
        break

print('-=-'*30)
print(f"{"Cod.":<10} {"Nome":<5} {"Média":<15}")
print('-'*20)
for i in range(0, len(boletin)):
    print(f'{i:<10} {boletin[i][0]:<5} {((boletin[i][1] + boletin[i][2]) / 2):<15.1f}')
print('-'*20)

tamanho_da_lista = len(boletin)
print(tamanho_da_lista)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? '))
    if mostrar < tamanho_da_lista and mostrar >= 0:
        print(f'Notas {boletin[mostrar][0]} são [{boletin[mostrar][1]:.1f}, {boletin[mostrar][2]:.1f}]')
    else:
        break
