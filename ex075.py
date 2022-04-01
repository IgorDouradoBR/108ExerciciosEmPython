n1 = int(input("digite o primeiro valor: "))
n2 = int(input("digite o segundo valor: "))
n3 = int(input("digite o terceiro valor: "))
n4 = int(input("digite o quarto valor: "))
tupla = n1, n2, n3, n4
pares = 0
for n in range(0, len(tupla)):
    if tupla[n]%2==0:
        pares += tupla[n]
print(pares)