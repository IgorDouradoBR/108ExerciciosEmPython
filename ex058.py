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
sleep(1)
cont = 0
umaT = "1 tentativa"
while jogador != pc:
    jogador = int(input("seu número é diferente do pensado pela maquina, tente outra vez, número: "))
    cont += 1
print ("parabéns, você acertou o número pensado pela maquina, no caso o número {}".format(pc))
if cont == 0:
    print("você acertou na ", umaT, " que sorte(ou hack)")
elif cont > 1:
    print("você acertou na {} ª tentativa".format(cont+1))