nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer {}!'.format(nome))

print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))