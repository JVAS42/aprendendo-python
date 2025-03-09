import exercicio115cadastros, exercicio115cadastrar

def menu():
    while True:
        print('-' * 40)
        print(f"{'MENU PRINCIPAL':^40}")
        print('-' * 40)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova Pessoa')
        print('3 - Sair do Sistema')
        print('-' * 40)
        opcao = int(input("Sua Opção: "))

        print(f"\n{'-' * 40}")
        print(f"{'-' * 40}")

        if opcao == 1:
            exercicio115cadastros.mostrar_cadastros()
        elif opcao == 2:
            exercicio115cadastrar.cadastrar_usuario()
        elif opcao == 3:
            print(f"{'Finalizando Programa':^40}")
            break
        else:
            print(f"{'Opção Não Encontrada':^40}")
            continue


