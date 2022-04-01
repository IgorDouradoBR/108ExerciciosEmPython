dias = float(input('digite os dias por quanto tempo o carro será alugado:'))
km = float(input('quanto quilometros irá rodar:'))
pago = (km * 0.15) + (dias * 60)
print('o total a pagar pelo carro é {:.2f}'.format(pago))