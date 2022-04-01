num = int(input("digite um número para saber seu fatorial: "))
cont = 1
for c in range(num):
    cont *= (c + 1)
print("o fatorial do número {} é {} ".format(num, cont))