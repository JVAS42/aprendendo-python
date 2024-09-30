num = 0
while True:
    num = int(input('Número para a tabuada [VALOR NEGATIVO QUANDO NÃO QUISER MAIS]: '))
    if num >= 0:
        print(f'TABUADA DO {num}')
        for c in range(1, 10):
            print(f'{c} x {num} = {c * num}')
    else:
        break
