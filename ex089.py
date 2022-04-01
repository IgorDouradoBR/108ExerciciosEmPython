lista = list()
listao = list()
nome = list()
num = 0
while True:
    nome = str(input(f"digite o nome do {num + 1} º aluno: "))
    nota1 = float(input(f"digite a 1ª nota do {num + 1} º aluno: "))
    nota2 = float(input(f"digite a 2ª nota do {num + 1} º aluno: "))

    lista.insert(0, nome)
    lista.insert(1, nota1)
    lista.insert(2, nota2)
    listao.insert(0, lista[0:3])

    num += 1

    SouN = str(input(
        "digite S se deseja continuar com o cadastro de alunos e N pra parar com o cadastro de alunos: ")).strip().upper()[
        0]
    while SouN not in 'SN':
        SouN = str(input(
            "repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de alunos: ")).strip().upper()[
            0]
    if SouN == 'N':
        break

for x, z in enumerate(listao):
    nome += listao[x][0]
    sorted(nome)
print(nome)
for i in range(0, len(nome)):
    for a, b in enumerate(listao):
        if nome[i] == listao[a][0]:
            listao.insert(i, nome[i])
print("Nº    Nome        Média")
print("=" * 35)
for c, v in enumerate(listao[:num]):
    media = (listao[c][1] + listao[c][2]) / 2
    print(f"{c + 1}    {listao[c][0]} {' ' * (15 - (len(listao[c][0])))} {media}")