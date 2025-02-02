def escreva(mensagem):
    print('~' * len(mensagem))
    print("\033[94m" + mensagem + "\033[m")  # Azul claro
    print('~' * len(mensagem))

