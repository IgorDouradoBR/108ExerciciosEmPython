lista =list()
vez = 0
while True:
  n1 = float(input(f"digite o {vez + 1} º valor: "))
  
  if n1 not in lista:
    lista.append(n1)
    print("valor adicionado")
    vez += 1 
  else:
    print("valor já existente na lista, digite outro")
  
  
  SouN  = str(input("digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores: ")).strip().upper()[0]
  while SouN not in 'SN':
      SouN  = str(input("repetindo... digite S se deseja continuar com o cadastro de pessoas e N pra parar com o cadastro de valores númericos: ")).strip().upper()[0]
  if SouN == 'N':
    break

lista.sort()  
print("lista de valores em ordem crescente: " , lista) 