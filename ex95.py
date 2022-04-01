dicio = dict()
lista = list()
i = 0
totalGol = 0
while True:
  nome = str(input(f"nome do jogador: "))
  dicio['nome'] = nome
  dicio['posicao'] = i + 1 
  partidas = int(input(f"numeros de partidas de {nome}: "))
  dicio['partidas'] = partidas
  for g in range(0, partidas):
      gol = int(input(f"quantos gols você marcou na {g+1}º rodada: "))
      lista.append(gol)
      totalGol+= gol
  dicio['gols por rodada'] = lista[:]
  dicio['total de gols'] = sum(lista)
  i += 1
  SouN = str(input(
        "digite S se deseja continuar com o cadastro de alunos e N pra parar com o cadastro de alunos: ")).strip().upper()[
        0]
  while SouN not in 'SN':
        SouN = str(input(
            "repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de alunos: ")).strip().upper()[
            0]
  if SouN == 'N':
        break

print("cod  nome     gols    total")
for c, v in dicio.items():
  if c != 'partida':
    
    print(f"{v}", end= '')
    
print("-="*30)
print(f"O jogador {dicio['nome']} jogou {dicio['partidas']} partidas")
for c, v in enumerate(dicio['gols por rodada']):
        print(f"  => na partida {c+1} fez {v} gols")
print(f"Foi um total de {dicio['total de gols']} gols")


