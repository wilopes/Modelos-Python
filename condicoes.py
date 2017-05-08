salarioMinimo = 880.00
salario = float(input("Digite seu salario: "))
temFilho = input("Voce tem filho? S - sim ou N - nao \n")
numeroFilhos = int(input("Digite o numero de filhos: "))
(temFilho == "S") and (salario < salarioMinimo)
ajudaFilho = 20.00
salario = salarioMinimo + (ajudaFilho * numeroFilhos)
print(salario)
