def fr(frase):
  tam = len(frase) + 6
  print("~" * tam)
  print(f"   {frase}")
  print("~" * tam)


lista = list()
while True:
  frases = str(input("digite uma frase: "))
  lista.append(frases)
  SouN = str(input(
        "digite S se deseja continuar adicionando frases e N pra parar de adicionar frases: ")).strip().upper()[
        0]
  while SouN not in 'SN':
        SouN = str(input(
            "repetindo... digite S se deseja continuar adicionando frases e N pra parar de adicionar frases: ")).strip().upper()[
            0]
  if SouN == 'N':
        break
for i in range(0, len(lista)):
  fr(lista[i])
  
