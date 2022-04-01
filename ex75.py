tupla = ( int(input("digite o primeiro valor: ")),
   int(input("digite o segundo valor: ")),
   int(input("digite o terceiro valor: ")),
   int(input("digite o quarto valor: ")))
print(f'você digitou os valores: {tupla}')
if 3 in tupla:
  print(f'o valor 3 apareceu pela primeira vez na {tupla.index(3)+1}ª posição')
else:
  print(f'o valor 3 nao apareceu nos valores digitados') 
print(f'o valor 9 apareceu {tupla.count(9)} vezes')

print("os valores pares são: ", end='')
for n in tupla:
    if n%2==0:
        print(' ', n, end='')
