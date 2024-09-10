nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2;

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('Aluno está APROVADO!')
elif media < 5:
    print('Aluno está REPROVADO!')
else:
    print('Aluno está RECUPERAÇÃO')