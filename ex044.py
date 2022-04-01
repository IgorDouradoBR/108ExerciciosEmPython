preco = float(input("digite o preço original do produto: "))
print("opções de pagamento: \n [1] À VISTA \n[2] DÉBITO \n[3] 2X NO CARTÃO \n[4] 3X OU MAIS NO CARTÃO ")
opcao = int(input("digite a opção escolhida: "))
if opcao == 1:
    precoFinal = preco * 0.9
    print (precoFinal, "R$")
elif opcao == 2:
    precoFinal = preco * 0.95
    print(precoFinal, "R$")
elif opcao == 3:
    precoFinal = preco
    parcela2 = preco / 2
    print("fica o preço normal: ", precoFinal, "R$, dividido em 2 parcelas de ", parcela2 ,"R$ cada")
elif opcao == 4:
    parcela = int(input("digite em quantas parcelas pretende dividir o produto "))
    precoFinal = preco * 1.20
    parcelado = precoFinal / parcela
    print("fica com um preco final de", precoFinal, "com parcelas mensais de: ", parcelado, "R$ em", parcela, "meses")
