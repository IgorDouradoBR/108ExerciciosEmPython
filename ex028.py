from random import randint
from time import  sleep
#nome = str(input('digite um numero para sorteio: '))
#numeros = nome[0, 5]
#sort = randint(nome)
pc = randint(0, 10)
print('*#-'*20)
print('to pensando em um numero de 0 a 10, se acertar ganha um biscoito')
print('*#-'*20)
jogador = int(input('que numero eu pensei pivete??'))
print('processando')
sleep(2)
if jogador == pc:
    print('parabéns viado')
else:
    print('perdeu, sua mãe é minha agora, eu pensei no {} e nao no {} otario'.format(pc, jogador))