from datetime import datetime


def maior_idade(a):
    from datetime import datetime # Escopo de importação
    idade = datetime.now().year - a
    if idade < 18:
        return False
    else:
        return True


ano = int(input('Em que ano você nasceu? '))
if maior_idade(ano) == False:
    print(f'Com {datetime.now().year - ano} anos: NÃO VOTA')
else:
    print(f'Com {datetime.now().year - ano} anos: VOTA')
