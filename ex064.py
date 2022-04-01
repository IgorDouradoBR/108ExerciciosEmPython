num = int(input("digite um valor inteiro, sabendo que se digitar o número 999 o programa parará: "))
parada = 999
cont = 0
soma = 0
while num != parada:
    cont += 1
    soma += num
    num = int(input("digite outro valor inteiro, sabendo que se digitar o número 999 o programa parará: "))
print("múmero de termos digitados até a parada do programa: {}".format(cont))
print("soma deles: {}".format(soma))