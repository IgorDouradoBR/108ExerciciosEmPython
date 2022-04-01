import random
n1 = str(input('primeiro aluno :'))
n2 = input('segundo aluno:')
n3 = input('terceiro aluno:')
n4 = str(input('quarto aluno :'))
lista = [n1, n2 ,n3 ,n4]
escolhido = random.choice(lista)
print('o aluno escolhido da lista foi {}'.format(escolhido))
ouuuu
from random import choice
n1 = str(input('primeiro aluno :'))
n2 = input('segundo aluno:')
n3 = input('terceiro aluno:')
n4 = str(input('quarto aluno :'))
lista = [n1, n2 ,n3 ,n4]
escolhido = choice(lista)
print('o aluno escolhido da lista foi {}'.format(escolhido))
