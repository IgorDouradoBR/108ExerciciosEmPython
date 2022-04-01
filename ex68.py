import random
vitorias = 0
while True:
  PouI = int(input("digite 1 se voce quer par e 2 se você deseja ser ímpar: "))
  numMaq = random.randrange(0, 10)
  numJog = int(input("digite o seu número : "))
  if (numJog + numMaq) % 2 != 0:
    if PouI == 2:
      print("parabéns, você venceu, ganhou mais uma ficha")
      vitorias += 1
    elif PouI == 1:
      print("você perdeu dessa vez, acabou por hoje")
      break
  if (numJog + numMaq) % 2 == 0:
    if PouI == 1:
      print("parabéns, você venceu, ganhou mais uma ficha")
      vitorias += 1
    elif PouI == 2:
      print("você perdeu dessa vez, acabou por hoje")
      break
print(f"número de vitórias seguidas: {vitorias}")