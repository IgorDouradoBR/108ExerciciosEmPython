n = int(input('digite um número'))
ant = n1 - 1
suc = n1 + 1
print('o antecessor de', n1, 'é', ant, 'e o sucessor é', suc)
-forma 100 correta
n1 = int(input('digite um número'))
print('o antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))