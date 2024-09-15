from random import randint

listaJogadas = ['Pedra', 'Papel', 'Tesouro']
maquina = randint(0,2)
print(maquina)
print('='*10+' JOGUINHO '+'='*10)
print('Sua opções:'+
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA')
jogada = int(input('Qual é a sua jogada? '))

if jogada == 0:
    if maquina == 0:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('EMPATE')
    elif maquina == 1:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ PERDEU')
    else:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ GANHOU')
elif jogada == 1:
    if maquina == 0:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ GANHOU')
    elif maquina == 1:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('EMPATE')
    else:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ PERDEU')
elif jogada == 2:
    if maquina == 0:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ PERDER')
    elif maquina == 1:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('VOCÊ GANHOU')
    else:
        print('Computador jogou {}'.format(listaJogadas[maquina]))
        print('Você jogou {}'.format(listaJogadas[jogada]))
        print('EMPATE')
else:
    print('ERRO404 - Opção não encontrada')
