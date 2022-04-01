def maior(lista):
    mai = 0
    for i in range(0, len(lista)):
        if lista[i]> mai:
            mai = lista[i]
    print(f"{lista} Foram informados {len(lista)} valores ao todo\nE o maior valor informado foi {mai}")


lista = list()
while True:
    valor = int(input("Digite um valor inteiro, sabendo que com 999 o cadastro para: "))
    if valor != 999:
        lista.append(valor)
    if valor == 999:
        break
maior(lista)
