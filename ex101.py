from datetime import datetime
def voto(dataN):
    ano=datetime.now().year
    if ano-dataN < 16:
        return 'NEGADO'
    elif 16 <= ano-dataN < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

param = int(input('digite o seu ano de nascimento: '))
print(f'situtação de voto: {voto(param)}')