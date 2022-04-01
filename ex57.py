sexo = str(input("digite seu sexo, com M para masculino e F para feminino: ")).strip().upper()[0]
while sexo not in 'MmFf':
  sexo = str(input("digite um sexo dentre os listados:  ")).strip().upper()[0]
print("o sexo {} foi registrado com sucesso ".format(sexo))