print('-='*20)
print('tipo de triângulo', ' (e sim, só tem essa recepção quando se trata de triângulo )')
print('-='*20)
r1 = float(input('digite o primeiro lado do triangulo: '))
r2 = float(input('digite o segundo lado do triangulo: '))
r3 = float(input('digite o terceiro lado do triangulo: '))
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as três retas PODEM formar um triangulo', end= '')
    if r1 == r2 and  r1== r3 and r2== r3 :
        print(' equilátero')
    elif r1 == r2 or  r1== r3 or r2== r3:
        print(' isóceles')
    else:
        print(' escaleno')
else:
    print('as três NÃo PODEM formar um triangulo')