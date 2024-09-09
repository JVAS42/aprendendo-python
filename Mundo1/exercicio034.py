salario = float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    novoSalario = (salario*110)/100
else:
    novoSalario = (salario*115)/100

print('Quem ganhava R${:.2f} pasa a ganhar R${:.2f} agora!'.format(salario, novoSalario))