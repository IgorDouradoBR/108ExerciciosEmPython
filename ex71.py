saque = int(input("digite o valor do saque: "))
n50 = saque//50
n20 = (saque%50)//20
n10 = ((saque%50)%20) // 10
n1 = (((saque%50)%20)%10) // 1
print(f"Total de {n50} de cédulas de 50 reais \n Total de {n20} de cédulas de 20 reais \nTotal de {n10} de cédulas de 10 reais \nTotal de {n1} de cédulas de 1 real \n")