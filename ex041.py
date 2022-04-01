from datetime import date

data = date.today()
anoAtual = data.year

ano = int(input("digite o seu ano de nascimento a seguir para \n saber sua categoria: "))
idade = anoAtual - ano
if idade <= 9:
    print("categoria: mirim")
elif idade > 10 and idade <= 14:
    print("categoria: infantil")
elif idade > 14 and idade <= 19:
    print("categoria: infantil")
elif idade == 20:
    print("categoria: senior")
elif idade > 20:
    print("categoria: master")