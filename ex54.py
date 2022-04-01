pessoas=7
menores=0
maiores=0
for i in range(pessoas):
  ano = float(input("digite o seu ano de nascimento: "))
  if ano<=2001:
    maiores += 1
  if ano>2001:
    menores += 1
print("quantidade de pessoas do grupo de maior: ", maiores)
print("quantidade de pessoas do grupo de menor: ", menores)