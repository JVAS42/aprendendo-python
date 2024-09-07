from random import randint

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

listaDeNomes = [n1, n2, n3, n4]
#escolhido  = random.choice(listaDeNomes)
numeroSorteado = randint(0,3)

print('O aluno escolhido foi {}'.format(listaDeNomes[numeroSorteado]))
