def fatorial(num, show=False):
    ret=1
    for c in range(num,0,-1):
        if show == True:
            if(c!=1):
                print(c, end=' x ')
            else:
                print(c, end=' = ')
            ret *= c
        else:
            ret *= c
    return ret

param = int(input('digite o numero para aplicar o fatorial: '))
print( fatorial(param,False))
