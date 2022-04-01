valor = float(input('digite a distância, em km, da sua viagem: '))
if valor <= 200:
    print('o valor da sua passagem é: {} R$'.format(valor * 0.5))
else:
    print('o valor da sua passagem é igual: {} R$'.format(valor * 0.45))