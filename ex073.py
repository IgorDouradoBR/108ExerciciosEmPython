times = 'Corinthians',   'Bahia', 'Atlético-MG', 'Botafogo', 'Ceará', 'Atlético-PR', 'Chapecoense',  'Cruzeiro', 'CSA', 'Flamengo',  'Fortaleza', 'Goiás',  'Avaí', 'Grêmio', 'Internacional', 'Palmeiras', 'Fluminense', 'São Paulo', 'Santos', 'Vasco'
print('Classicação final: ')
for c in range(0, len(times)):
    print(f'{(c+1)} º - {times[c]} \n')
while True:
    opt = int(input("digite o número da opção que voce quer saber: \n[1]os 5 primeiros colocados do brasileirão\n[2]os últimos 4 colocados do brasileirão\n[3]ordem alfabética dos times\n[4]em que posição o time da Chapecoense está\n[0] para sair do programa"))
    if opt == 1 :
        print(f'os 5 primeiros colocados em ordem de classificação: {times[0:5]} ')
    if opt == 2:
        print(f'os 4 últimos colocados em ordem de classificação: {times[-4:]} ')
    if opt == 3:
        print(f"a listagem dos times em ordem alfabética: {sorted(times)}")
    if opt == 4:
        for c in range(0, len(times)):
            if times[c] == 'Chapecoense':
                print(f'a chapecoense está na {c+1} colocação')
    if opt == 0:
        break