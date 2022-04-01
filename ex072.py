extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    numero = int(input("digite um número de 0 a 20 (se digitar fora desse intervalo o programa parará) para saber seu correspondente: "))
    print(f'o {numero} por extenso é: {extenso[numero]}')
    if numero < 0 or numero > 20:
        break



















