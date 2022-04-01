vel = float(input('velocidade a que você estava na hora? '))
if vel >= 80:
    print('voce foi multado no valor de {} R$, vagabundo'.format((vel - 80) * 7))
else:
    print('deu sorte hein malandro')