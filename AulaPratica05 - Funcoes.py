#funções
def produtos():
    produtosVenda = {"smartv": 1000.00, "dvd": 100.00, "pendrive": 50.00}
    return produtosVenda
    
def comprarProduto(opcao):
    carrinho = {}
    prod = produtos()
    print("Produtos Disponíveis")
    print(prod)
    while (opcao!="nao"):
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        
        preco = prod[nomeProduto]
        
        carrinho[nomeProduto] = quantidade, preco, preco*quantidade
        print("Carrinho: ")
        print(carrinho)
        
        opcao = input("Deseja comprar mais produtos? sim ou não: ")
    return carrinho
    
def calcularTotal(carrinho):
    total = 0
    for produto in carrinho:
        total = total + carrinho[produto][2]
    print("Total de compra: %f"%(total))
    return total
