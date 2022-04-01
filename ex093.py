dicio = dict()
lista = list()
i = 0
totalGol = 0
dicio['nome'] = str(input(f"nome do jogador: "))
partidas = int(input(f"numeros de partidas: "))
dicio['partidas'] = partidas
for g in range(0, partidas):
    gol = int(input(f"quantos gols você marcou na {g+1}º rodada: "))
    lista.append(gol)
    totalGol+= gol
dicio['gols por rodada'] = lista[:]
dicio['total de gols'] = sum(lista)
print("-="*30)
print(dicio)
print("-="*30)
for c, v in dicio.items():
    print(f"{c} = {v}")
print("-="*30)
print(f"O jogador {dicio['nome']} jogou {dicio['partidas']} partidas")
for c, v in enumerate(dicio['gols por rodada']):
        print(f"  => na partida {c+1} fez {v} gols")
print(f"Foi um total de {dicio['total de gols']} gols")


