tupla = 'Nutella', 35.75, 'café da Dolce Gusto', 34.90, 'papel higiênico Neve', 6.59, 'amaciante Comfort', 12.98, 'ração Pedigree', 15.98, 'ketchup Heinz', 8.59, 'Listerine 1l', 50.30

for n in range(0, len(tupla)):
  if n%2==0:
    print(f'{tupla[n]:.<30}', end='')
  else:
    print(f'{tupla[n]:>7.2f}')

