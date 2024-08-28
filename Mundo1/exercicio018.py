import math

angulo = int(input('Digite o ângulo que você deseja: '))
radiano = math.radians(angulo)

print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, math.sin(radiano)))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, math.cos(radiano)))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, math.tan(radiano)))
