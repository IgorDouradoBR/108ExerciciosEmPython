frase = str(input('digite uma frase:')).upper().strip()
print('A aparece {} vezes'.format(frase.count('A')))
print('o 1º A apareceu na posicao {}'.format(frase.find('A')+1))
print('a ultima letra "A" apareceu na posiçao {}'.format(frase.rfind('A')+1))