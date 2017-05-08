"""
Spyder Editor

This is a temporary script file.
"""
#Modulo principal
import realizarCompras

def descontoValor(total):
    if total>=1000:
        print("Você ganhou 20 por cento de desconto")
        desconto = 0.2*total
    else:
        print("So ha desconto para compras acima de 1000")
        desconto = 0
    return desconto

def main():
    opcao = input("Deseja comprar um produto? sim ou nao: ")
    carrinhoCompras = realizarCompras.comprarProduto(opcao)
    total = realizarCompras.calcularTotal(carrinhoCompras)
    excluir = input("Deseja excluir produtos do carrinho? sim ou nao: ")
    while excluir== "sim":
        nomeProduto = input("Digite o produto a ser excluido: ")
        realizarCompras.excluirProdutos(nomeProduto, carrinhoCompras)
        total = realizarCompras.calcularTotal(carrinhoCompras)
        excluir = input("Deseja excluir produtos do carrinho? sim ou nao: ")
        
    desconto1 = descontoValor(total)

    total = total - desconto1
    print("Novo total: %.2f"%(total))

main()
