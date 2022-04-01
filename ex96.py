def area(larg, comp):
  res = larg * comp
  print(f"A área de um terreno retangular {larg}x{comp} é de {res}m²")


largura = float(input("digite a largura do terreno: "))
comp = float(input("digite o comprimento do terreno: "))
area(largura, comp)
