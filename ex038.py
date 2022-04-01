n1 = float(input("digite o primeiro valor inteiro: "))
n2 = float(input("digite o segundo valor inteiro: "))

num1 = n1 // 1
num2 = n2 // 1

if num1>num2:
    print( "o numero {:.0f} é maior que o {:.0f}".format(num1, num2))
elif num1 < num2:
    print("o numero {:.0f} é maior que o {:.0f}".format(num2, num1))
elif num1 == num2 :
    print("os números possuem o mesmo valor")