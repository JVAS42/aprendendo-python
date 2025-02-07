import exercicio108modulos

def leia_inteiro(msg):
    valor = input(msg).strip()
    while True:
        if valor.isnumeric():
            valor  = float(valor.replace(",", "."))
            return valor
        else:
            print(f"\033[31mERRO! {valor} é um preço inválido!\033[m")
            valor = input(msg)