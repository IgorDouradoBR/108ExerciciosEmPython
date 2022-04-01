import  random
n1 = str(input('primeiro aluno :'))
n2 = input('segundo aluno:')
n3 = input('terceiro aluno:')
n4 = str(input('quarto aluno :'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a orden de apresentacao será:')
print(lista)
ouuuu
from random import shuffle
n1 = str(input('primeiro aluno :'))
n2 = input('segundo aluno:')
n3 = input('terceiro aluno:')
n4 = str(input('quarto aluno :'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a orden de apresentacao será:')
print(lista)