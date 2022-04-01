from datetime import date

data = date.today()
anoAtual = data.year

ano = int(input("digite o seu ano de nascimento a seguir para saber se já é necessário você se alistar no exército: "))

if anoAtual - ano <= 17:
    print("você nao precisa capinar a cidade ainda")
elif anoAtual - ano == 18:
    print("já tá hominho, pode se alistar")
elif anoAtual - ano >= 19:
    print("já passou do tempo de se alistar")