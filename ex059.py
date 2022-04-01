num1 = float(input("digite o primeiro valor: "))
num2 = float(input("digite o segundo valor: "))
opt = int(input("digite o número correspondente à operação que deseja fazer com esses dois valores: \n [1] soma \n [2] subtração \n [3] multiplicação \n [4] divisão \n [5] sair do programa\n digite aqui o numero da opçao que deseja: "))
while opt < 1 or opt > 5:
    opt = int(input("digite uma das opções informadas acima \n opção: "))
while opt >= 1 and  opt <= 5:
    if opt == 1:
        print("resultado da soma: ", num1+num2)
    elif opt == 2:
        print("resultado da subtração: ", num1-num2)
    elif opt == 3:
        print("resultado da multiplicação: ", num1*num2)
    elif opt == 4:
        print("resultado da divisão: ", num1/num2)
    elif opt == 5:
        break
    rep = int(input("deseja fazer mais alguma operação? ([1] para sim e [2] para não) "))
    if rep == 1:
        opt = int(input("digite o número da outra opção que deseja realizar com esses números: "))
    if rep == 2:
        break
