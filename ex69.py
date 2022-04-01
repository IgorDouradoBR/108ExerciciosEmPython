
deMenor = homens = mulheres20 = 0
while True:
  idade = int(input(" digite sua idade: "))
  
  while idade < 0 or idade > 120:
    idade  = int(input("tu não é imortal fdp, digite a certa: "))
  sexo  = str(input(" digite seu sexo com M para masculino e F para feminino: ")).strip().upper()[0]
  while sexo not in 'MF':
    sexo  = str(input("digite uma das opções dadas, M para masculino e F para feminino: ")).strip().upper()[0]
  if idade > 18:
    deMenor += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20 :
    mulheres20 += 1
  SouN  = str(input("digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro: ")).strip().upper()[0]
  while SouN not in 'SN':
      SouN  = str(input("repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro: ")).strip().upper()[0]

  if SouN == 'N':
    break
print(f"Há {deMenor} pessoas com menos de 18 anos \nUm total de {homens} de homens\nE {mulheres20} mulheres com menos de 20 anos ")