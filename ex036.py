casa = float (input('digite o valor da casa desejada: '))
salario = float (input('digite o seu salário: '))
meses = int (input('digite em quantos meses você pretende quitar a casa: '))
prestacao = casa / meses
if prestacao < salario * 0.30:
    print("você pode parcelar sem medo pai")
elif prestacao >= salario * 0.30:
    print("nao dá, aí você vai se enrolar man")