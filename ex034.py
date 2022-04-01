sal = float(input('digite aqui o seu salário para saber o seu aumento: '))
if sal > 1250:
    print('seu novo salario é de: {:.3f} R$'.format(sal * 1.10))
else:
    print('seu novo salário é de: {:.3f} R$'.format(sal * 1.15))