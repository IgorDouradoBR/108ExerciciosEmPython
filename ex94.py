dados = dict()
lista = list()
nomes = list()
somaDeIdade = 0
while True:
  dados['nome'] = str(input(f"digite seu nome: "))
  dados['sexo'] = int(input(f"digite seu sexo, com 1 para masculino ou 2 para feminino: "))
  while dados['sexo'] > 2 or dados['sexo'] < 1:
    dados['sexo'] = int(input(f"repetindo... digite seu sexo, com 1 para masculino ou 2 para feminino: "))
  dados['idade'] = int(input(f"digite sua idade: "))
  if dados['sexo'] == 2:
    nomes.append(dados['nome'])
  somaDeIdade += dados['idade']
  lista.append(dados)
  SouN = str(input(
        "digite S se deseja continuar com o cadastro de alunos e N pra parar com o cadastro de alunos: ")).strip().upper()[
        0]
  while SouN not in 'SN':
        SouN = str(input(
            "repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de alunos: ")).strip().upper()[
            0]
  if SouN == 'N':
        break
print(f"Número de pessoas cadastradas: {   len(lista) } pessoas")   

  
mediaIdade = somaDeIdade / len(lista)
print(f"média de idade: {mediaIdade} anos")
print(f"lista com o nome de todas as mulheres: {nomes}")
print("lista com o nome das pessoas com idade acima da média: ", end = ' ')

for p in lista:
  if p['idade'] > mediaIdade:
    for c, v in p.items():
      print(f" {c} = {v}")
    print()
          



      