peso = float(input('Informe seu peso em KG: '))
altura = float(input('Informe sua altura em M: '))

imc = peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso IDEAL')
elif imc > 25 and imc <= 30:
    print('Você está com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')