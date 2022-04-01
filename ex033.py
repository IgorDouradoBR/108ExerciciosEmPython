n1 = float(input('digite o seu primeiro número:'))
n2 = float(input('digite o seu segundo número:'))
n3 = float(input('digite o seu terceiro número:'))
if n1 > n2 and n1 > n3 and n2 > n3:
    print('o {} é o maior e {} o menor'.format(n1, n3))
if n2 > n1 and n2 > n3 and n1 > n3:
    print('o {} é o maior e {} o menor'.format(n2, n3))
if n2 > n3 and n2 > n1 and n3 > n1:
    print('o {} é o maior e {} o menor'.format(n2, n1))
if n3 > n2 and n3 > n1 and n2 > n1:
    print('o {} é o maior e {} o menor'.format(n3, n1))
if n3 > n2 and n3 > n1 and n1 > n2:
    print('o {} é o maior e {} o menor'.format(n3, n2))
if n1 > n3 and n1 > n2 and n3 > n2:
    print('o {} é o maior e {} o menor'.format(n1, n2))
else:
    print('digite só número aí, meu patrão')