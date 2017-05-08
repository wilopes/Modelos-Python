compras = []
while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	compras.append([produto, quantidade, preco])

soma = 0
for e in compras:
    total = e[1] * e[2] #qtd x preco
    print(e[0], e[1], e[2], total)
    soma = soma + total
print("Total: %d" %(soma))
