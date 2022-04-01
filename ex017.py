import math
opo = int(input('digite o valor do cateto oposto'))
adj = int(input('digite o valor do cateto adjcente'))
hipotenusa = (opo ** 2) +  (adj ** 2)
print(' o valor da hipotenusa será de', hipotenusa ** (1/2))
essa deu certo kkkk mas a 100 correta é:
opo = float(input('digite o valor do cateto oposto'))
adj = float(input('digite o valor do cateto adjcente'))
hip = (opo **2 + adj ** 2) ** (1/2)
print('a hipotenusa valerá {:.2f}'.format(hip))
ou melhor ainda
opo = float(input('digite o valor do cateto oposto'))
adj = float(input('digite o valor do cateto adjcente'))
hipot = math.hypot(opo, adj)
print('a hipotenusa valerá {:.2f}'.format(hipot))