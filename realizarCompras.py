"""
Spyder Editor

This is a temporary script file.
"""
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
    print("Total de compra: %.2f"%(total))
    return total

def excluirProdutos(nomeProduto, carrinho):
    del carrinho [nomeProduto]
'''
>>> produtos()
{'smartv': 1000.0, 'dvd': 100.0, 'pendrive': 50.0}
>>> opcao = 'sim'
>>> carrinhoCompras = comprarProduto(opcao)
Produtos Disponíveis
{'smartv': 1000.0, 'dvd': 100.0, 'pendrive': 50.0}
Digite o nome do produto: dvd
Digite a quantidade: 3
Carrinho: 
{'dvd': (3, 100.0, 300.0)}
Deseja comprar mais produtos? sim ou não: sim
Digite o nome do produto: pendrive
Digite a quantidade: 2
Carrinho: 
{'dvd': (3, 100.0, 300.0), 'pendrive': (2, 50.0, 100.0)}
Deseja comprar mais produtos? sim ou não: nao
>>> calcularTotal(carrinhoCompras)
Total de compra: 400.000000
400.0
'''
