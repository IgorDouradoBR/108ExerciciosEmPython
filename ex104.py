def leiaInt(msg):
    ok=False
    while True:
        v = input('Digite um número: ')
        if v.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return v


n = leiaInt('Numero: ')
print(f'Você acabou de digitar o número {n}')