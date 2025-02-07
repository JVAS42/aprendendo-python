def notas(* notas, situação=False):
    '''
    → Função para analisar notas de alunos
    :param notas: Recebe uma tuplas de notas
    :param situação: (Opcional; Default = False). Verifica média e retorna situação(Ruim, Média, Boa)
    :return: Bolentin com Dicionário
    '''
    boletin_aluno = dict()
    media = 0
    boletin_aluno['total'] = len(notas)
    for i in range(0, len(notas)):
        if i == 0:
            boletin_aluno['maior'] = notas[i]
            boletin_aluno['menor'] = notas[i]
        else:
            if boletin_aluno['maior'] < notas[i]:
                boletin_aluno['maior'] = notas[i]
            if boletin_aluno['menor'] > notas[i]:
                boletin_aluno['menor'] = notas[i]
        media = media + notas[i]
    media = media/len(notas)
    boletin_aluno['media'] = media
    if situação == True:
        if boletin_aluno['media'] >= 7.0:
            boletin_aluno['situação'] = 'Boa'
        elif boletin_aluno['media'] >= 5.0:
            boletin_aluno['situação'] = 'Razoável'
        else:
            boletin_aluno['situação'] = 'Ruim'

    return boletin_aluno


help(notas)
resp = notas(5.5, 9.5, 10, 6.5, situação=True)
print(resp)
