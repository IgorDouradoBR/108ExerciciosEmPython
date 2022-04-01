lista = list()
for i in range(0, 5):
  lista.append(int(input(f"digite o {i+1}º valor: ")))
maior = 0
menor = 0
posMai = 0
posMen = 0
for i, j in enumerate(lista):
  if j< menor or menor == 0:
    menor = j
    posMen = i + 1
  if j> maior or maior == 0:
    maior = j
    posMai = i +1
print(f"o maior valor da lista é o {maior} que está na posição {posMai}ª")
print(f"e o menor valor da lista é o {menor} que está na posição {posMen}ª")
