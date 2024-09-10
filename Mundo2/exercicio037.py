valor = int(input('Digite um número  inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(valor)
    print('{} convertido para BINARIO é igual {}'.format(valor, binario))
elif escolha == 2:
    octal = oct(valor)
    print('{} convertido para BINARIO é igual {}'.format(valor, octal))
elif escolha == 3:
    hexadecimal = hex(valor)
    print('{} convertido para BINARIO é igual {}'.format(valor, hexadecimal))
else:
    print('Opção não encontrado!\nERRO.')