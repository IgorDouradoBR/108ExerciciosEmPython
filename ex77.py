palavras = 'Pneumoultramicroscopicossilicovulcanoconiótico', 'Paraclorobenzilpirrolidinonetilbenzimidazol ',  'Piperidinoetoxicarbometoxibenzofenona ', 'Tetrabrometacresolsulfonoftaleína ', 'homem', 'tempo', 'coisa', 'tempo', 'melhor', 'certo', 'grande', 'poder', 'muito'
for n in range(0, len(palavras)):
  print(f"a palavra '{palavras[n]}' tem as vogais: ", end=' ')
  if 'a' in palavras[n]:
    print("a", end=' ')
  if 'e' in palavras[n]:
    print("e", end=' ')
  if 'i' in palavras[n]:
    print("i", end=' ')
  if 'o' in palavras[n]:
    print("o", end=' ')
  if 'u' in palavras[n]:
    print("u", end=' ')
  print("\n")