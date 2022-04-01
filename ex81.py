lista =list()
par = list()
impar = list()
num = 0
while True:
  n1 = int(input(f"digite o {num + 1} º valor: "))
  lista.append(n1)
  if n1 % 2 == 0:
    par.append(n1)
  else:
    impar.append(n1)
  num += 1
  
  SouN  = str(input("digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores: ")).strip().upper()[0]
  while SouN not in 'SN':
      SouN  = str(input("repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores númericos: ")).strip().upper()[0]
  if SouN == 'N':
    break
lista.sort()
par.sort()
impar.sort()

print("lista com todos os numeros: ", lista)
print("lista com os numeros pares: ", par)
print("lista com os numeros ímpares: ", impar)