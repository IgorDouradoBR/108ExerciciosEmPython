import random
print("-="*6, "Aqui você tem os números da sorte", '-='*6)
lista = list()
numeros = list()
num = int(input("Quantos jogos serão feitos?? "))
i=0
while i<num:
  for c in range(0,6): 
    numeros.insert(c, random.randrange(1, 61))
  lista.insert(i, numeros[0:6])
  i+=1
for c in range(0, len(lista)):
  lista[c].sort()
  print(f"números do {c+1}º jogo: {lista[c]}")
    
