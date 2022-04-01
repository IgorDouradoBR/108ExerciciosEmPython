

altura = float(input("digite a sua altura: "))
peso = float(input("digite o seu peso: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("categoria: abaixo do peso ideal ")
elif imc >= 18.5 and imc < 25:
    print("categoria: peso ideal")
elif 25 <= imc < 30:
    print("categoria: sobrepeso")
elif imc >= 30 and imc < 40:
    print("categoria: obesidade")
elif imc >= 40:
    print("categoria: obesidade mórbida")