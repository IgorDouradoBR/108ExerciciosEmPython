num = float(input("digite um número(caso seja 999 o programa parará): "))
soma = cont = 0

while True:
  num = float(input("digite outro número(caso seja 999 o programa parará): "))
  if num == 999:
    break
  cont += 1
  soma += num  
print(f"a soma dos {cont} primeiros valores é de {soma}")