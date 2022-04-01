pessoas=5
maiorP=0
menorP=0
for i in range(pessoas):
  peso= float(input("digite o seu peso: "))
  if peso > maiorP:
    maiorP= peso
  if peso < menorP or menorP == 0:
    menorP= peso
print("maior peso: ", maiorP, " kg")
print("menor peso: ", menorP, " kg")