def leia_inteiro(msg):
    numero = input(msg)
    while True:
        if numero.isnumeric():

            return numero
        else:
            print("\033[31mERRO! Digite um número inteiro válido!\033[m")
            numero = input(msg)


n = leia_inteiro('Digite um número: ')
print(f'Você digitou o número {n}')
