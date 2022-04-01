import time


def contagem(inic, fim, passo):
    if passo>= 1 and inic>fim:
        posit = passo * -1
        for i in range(inic, fim-1, posit):
            print(i, end=' ')
            time.sleep(0.6)
    if passo>= 1 and inic<=fim:
        for i in range(inic, fim+1, passo):
            print(i, end=' ')
            time.sleep(0.6)
    elif passo < 0 and inic>fim:
        for i in range(inic, fim-1, passo):
            print(i, end=' ')
            time.sleep(0.6)
    elif passo < 0 and fim >= inic:
        posit = passo * -1
        for i in range(fim, inic+1, posit):
            print(i, end=' ')
            time.sleep(0.6)
    elif passo == 0 and fim >= inic:
        for i in range(fim, inic+1, 1):
            print(i, end=' ')
            time.sleep(0.6)
    elif passo == 0 and fim < inic:
        for i in range(inic, fim-1, -1):
            print(i, end=' ')
            time.sleep(0.6)


print("-=" * 23)
print("Contagem de 0 até 10 de 1 em 1: ")
for i in range(0, 11):
    print(i, end=' ')
    time.sleep(0.6)
print("FIM!")
print("-=" * 23)
print("Contagem de 10 até 0 de 2 em 2: ")
for i in range(10, -1, -2):
    print(i, end=' ')
    time.sleep(0.6)
print("FIM!")
print("-=" * 23)
print("")
print("Agora é sua vez, digite o início, fim e o passo(de quanto em quanto): ")
inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
contagem(inicio, fim, passo)
print("FIM!")
