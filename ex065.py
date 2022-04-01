num1 = float(input("digite valores para no final saber o maior deles, o menor e a média entre eles: "))
outro = str(input("digite SIM se quiser adicionar outro número e NÃO se já for o suficiente: "))
sim = 'SimSIMsim'
cont = 1
maiorV = num1
menorV = num1
soma = num1
while outro in sim:
    num2 = float(input("digite o outro valor: "))
    if num2 < menorV:
        menorV = num2
    if num2 > maiorV:
        maiorV = num2
    soma += num2
    cont += 1
    outro = str(input("digite SIM se quiser adicionar outro número e NÃO se já for o suficiente: "))

media = soma / cont
print("média entre os números informados {}".format(media))
print("menor valor entre os números informados {}".format(menorV))
print("maior valor entre os números informados {}".format(maiorV))