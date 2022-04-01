import math
ângulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ângulo))
print('o ângulo citado de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('o ângulo citado de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('o ângulo citado de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
OOOUUU
from math import radians, sin, cos, tan
ângulo = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(ângulo))
print('o ângulo citado de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('o ângulo citado de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('o ângulo citado de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
