import random
lista = list()
lista2 = list()
def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
          if lista[i] > lista[i+1]:
               lista[i], lista[i+1] = lista[i+1],lista[i]
               ordenado = False
        print(lista)
    return lista




dicio = {f'q': random.randint(1, 6),
        f'w': random.randint(1, 6),
        f'e': random.randint(1, 6),
        f'd': random.randint(1, 6)}

lista2.append(dicio.values())
lista2 = lista2
print(lista2)

