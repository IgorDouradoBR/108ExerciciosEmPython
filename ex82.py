lista =list()
num = 0
while True:
  n1 = float(input(f"digite o {num + 1} º valor: "))
  lista.append(n1)
  num += 1
  
  
  SouN  = str(input("digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores: ")).strip().upper()[0]
  while SouN not in 'SN':
      SouN  = str(input("repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores númericos: ")).strip().upper()[0]
  if SouN == 'N':
    break
print(f"foram digitados {num} valores")
lista.sort(reverse =True)  
print("lista de valores em ordem decrescente: " , lista) 
for c, v in enumerate(lista):
  if v == 5:
    print("o valor 5 está na lista na posição ", c+1 )
if 5 not in lista: 
  print("o 5 nao está entre os valores digitados")