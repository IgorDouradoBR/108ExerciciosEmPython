aberto = 0
fechado = 0
frase = str(input("digite uma expressão contendo todos os parênteses fechados: "))
for c in frase:
  if c == '(':
    aberto += 1
  if c == ')':
    fechado += 1
if aberto == fechado or aberto == 0 and fechado ==0 :
  print("expressão válida")
else: 
  print("expressão inválida")