pessoas=4
maisVelho=0
mulheres20=0

soma = 0
nomeVel = ""
for i in range(pessoas):
  idade = int(input("digite sua idade: "))
  soma+= idade
  sexo = int(input("para [0] para masculino e [1] para feminino, digite o seu sexo:  "))
  nome= str(input("digite o seu nome: "))
  if idade > maisVelho:
    maisVelho = idade
    nomeVel = nome
  if idade < 20 and sexo == 1:
    mulheres20 += 1
media = soma / pessoas
print("media de idade do grupo: ", media)
print("nome do mais velho do grupo: ", nomeVel)
print("quantidade de mulheres com menos de 20 anos: ", mulheres20)

