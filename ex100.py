import random
import time
lista = list()

def numeros():
    i=0
    print(f"Sorteando 5 valores da lista: ", end= ' ')
    while i < 5:
        elem = random.randint(0, 10)
        time.sleep(0.4)
        print(elem, end= ' ')
        lista.append(elem)
        i += 1
    print(" PRONTO!")

def soma():
    somaPar = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            somaPar += lista[i]
    print(f"Somando os valores pares da lista {lista} temos o total de {somaPar}")


numeros()
soma()






