num = int(input('Informe o número: '))
numFat = num
fat = 1

while num > 1:
    fat = num * fat
    num = num - 1

print('{}!'.format(numFat),end=' = ')
for c in range(numFat, 1, -1):
    print('{}'.format(c), end='x')
print('1 = {}'.format(fat))