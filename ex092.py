dicio = dict()
lista = list()
nome = str(input(f"seu nome"))
dicio['nome'] = nome
ano = int(input(f"ano de nascimento: "))
while ano>2019 or ano<1900:
    ano = int(input(f"digite um ano de nascimento válido: "))
dicio['ano'] = ano
idade = 2019 - ano
dicio['idade'] = idade

carteira = int(input(f"carteira de trabalho(0 se não tiver): "))
if carteira> 0:
    dicio['carteira'] = carteira
    anoC = int(input(f"ano de sua primeira contratação: "))
    while ano > 2019 or ano < 1900 or anoC < ano:
        anoC = int(input(f"digite um ano válido para sua contratação: "))
    dicio['ano de contratação'] = anoC
    salario = float(input(f"Seu salário: "))
    dicio['salário'] = salario
    aposent = (anoC-ano) + 35
    dicio['aposent'] = aposent
for c, v in dicio.items():
        print(f"{c} = {v}")









