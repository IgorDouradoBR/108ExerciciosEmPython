from random import randrange
n1 = randrange(0, 1000)
n2 = randrange(0, 1000)
n3 = randrange(0, 1000)
n4 = randrange(0, 1000)
n5 = randrange(0, 1000)
tupla = n1, n2, n3, n4, n5
print('números gerados: ', tupla)
ordem = sorted(tupla)
print(f'maior valor da tupla: {ordem[-1]}')
print(f'menor valor da tupla: {ordem[0]}')

