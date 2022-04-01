p1 = float(input("digite a nota da sua primeira prova: "))
p2 = float(input("digite a nota da sua segunda prova: "))

media = (p1 + p2) / 2

if media < 5:
    print("reprovado vagabundo")
elif media >=5 and media < 7:
    print("tá na recuperação, ainda há um fio de esperança")
elif media >= 7:
    print("passou direto nerd")