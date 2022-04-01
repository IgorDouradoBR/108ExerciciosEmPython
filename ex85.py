lista = list()
par = list()
impar = list()
for i in range(0, 7):
  num = int(input(f"digite o {i + 1} º valor: "))
  if num % 2 == 0:
    par.append(num)
  if num % 2 != 0:
    impar.append(num)
lista.append(par)
lista.append(impar)
lista[0].sort()
lista[1].sort()
if len(par) > 0 and len(impar) > 0:
  print(f"valores pares digitados em ordem crescente: {lista[0]}.")
  print(f"valores ímpares digitados em ordem crescente: {lista[1]}.")
if len(par) == 0:
    print(f"valores ímpares digitados em ordem crescente: {lista[1]}.")
if len(impar) == 0:
    print(f"valores pares digitados em ordem crescente: {lista[0]}.")

