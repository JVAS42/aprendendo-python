def leia_inteiro(msg):
    while True:
        try:
            i = int(input(msg))
        except(ValueError):
            print("\033[31mERRO! Digite um número inteiro válido!\033[m")
            continue
        else:
            return i


def leia_float(msg):
    while True:
        try:
            f = float(input(msg))
        except(ValueError):
            print("\033[31mERRO! Digite um número real válido!\033[m")
            continue
        else:
            return f


i = leia_inteiro('Digite um número inteiro: ')
f = leia_float('Digite um número real: ')
print(f'Você informou o número inteiro {i} e o número real {f}')
