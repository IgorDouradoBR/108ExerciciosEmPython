
gastoT = maisDeMil= barato = 0
baratoNome = ''
while True:
  nome  = str(input(" digite o nome deste produto: "))
  preco = float(input(" digite o preço do produto: "))

  
  gastoT += preco
  if preco > 1000:
    maisDeMil += 1
  if preco < barato or barato == 0:
    barato = preco
    baratoNome = nome
  SouN  = str(input("digite S se deseja continuar a comprar e cadastrar produtos e N pra parar com as compras: ")).strip().upper()[0]
  while SouN not in 'SN':
    SouN  = str(input("Repetindo... digite S se deseja continuar a comprar e cadastrar produtos e N pra parar com as compras: ")).strip().upper()[0]
  if SouN == 'N':
    break
print(f"Gasto total: {gastoT}R$ \n{maisDeMil} produtos custam mais de mil reais\n{baratoNome} é o produto mais barato ")