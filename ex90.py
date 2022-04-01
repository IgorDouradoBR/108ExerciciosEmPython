dicio = dict()
lista = list()
i = 0

while True:
    nome = str(input(f"digite seu nome: "))
    dicio['nome'] = nome
    nota1 = float(input(f"digite sua 1ª nota, {nome}: "))
    nota2 = float(input(f"digite sua 2ª nota, {nome}: "))
    media = (nota1 + nota2) / 2
    dicio['media'] = media
    lista.insert(0, dicio.copy())
    i += 1
    opt = int(input("digite 1 se você quer saber apenas sua nota ou 2 se quiser saber a média dos alunos cadastrados: "))
    while opt != 1 and opt!= 2:
        opt = int(
            input("repetindo... digite 1 se você quer saber apenas sua nota ou 2 se quiser saber a média dos alunos cadastrados: "))
    if opt == 1:
        for p in lista:
            for c, v in p.items():
                if p == lista[0]:
                    print(f"{c} = {v}")
    if opt == 2:
        print("Nome              Média")
        for p in lista:
            for c, v in p.items():
                if c == 'nome':
                    print(f"{v}{' ' * (11-len(v)) } = {' ' * 2} ", end=' ')

                if c == 'media':
                    print(f"{v}")
    SouN = str(input(
        "digite S se deseja continuar com o cadastro de alunos e N pra parar com o cadastro de alunos: ")).strip().upper()[
        0]
    while SouN not in 'SN':
        SouN = str(input(
            "repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de alunos: ")).strip().upper()[
            0]
    if SouN == 'N':
        break


