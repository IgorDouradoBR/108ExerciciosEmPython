print('-='*20)
print('analisador de triângulos')
print('-='*20)
r1 = float(input('digite o primeiro lado do triangulo: '))
r2 = float(input('digite o segundo lado do triangulo: '))
r3 = float(input('digite o terceiro lado do triangulo: '))
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as três retas PODEM formar um triangulo')
else:
    print('as três NÃo PODEM formar um triangulo')