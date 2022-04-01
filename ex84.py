nomePeso =list()
pesos = list()
num = 0
pessoas = 0
while True:
  nome = str(input(f"digite o nome da {num + 1}ª pessoa: "))
  nomePeso.append(nome)
  
  peso = int(input(f"digite o peso da {num + 1}ª pessoa: "))
  nomePeso.append(peso)
  pesos.append(peso)
  
  num += 1
  pessoas += 1
  SouN  = str(input("digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores: ")).strip().upper()[0]
  while SouN not in 'SN':
      SouN  = str(input("repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores númericos: ")).strip().upper()[0]
  if SouN == 'N':
    break
print(f"foram cadastradas {pessoas} pessoas")
maisLev = 0
pesos.sort()
if pessoas >= 3:
  print("as 3 pessoas mais leves: ")
else:
  print("as pessoas mais leves são:")
for c, v in enumerate(pesos):
  for i in range(0, len(nomePeso)):
    if pesos[c] == nomePeso[i] and maisLev<3:
      print(nomePeso[i-1], "pesando ", v , " kg" , end = ' ')
      maisLev += 1
maisPes = 0
pesos.sort(reverse = True)
if pessoas >= 3:
  print("as 3 pessoas mais pesadas: ")
else:
  print("as pessoas mais pesadas são:")
for c, v in enumerate(pesos):
  for i in range(0, len(nomePeso)):
    if pesos[c] == nomePeso[i] and maisPes<3:
      print(nomePeso[i-1], "pesando ", v , " kg;" , end = ' ')
      maisPes += 1




