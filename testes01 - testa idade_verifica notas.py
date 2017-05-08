#Verificar Idade
idade = int(input("qual a idade: "))

if (idade < 12):
  
	print("crianca")

elif (idade >= 12) and (idade <= 18):

	print("adolescente")

else:

	print("adulto")

#somar notas
totalProvas = 3

i = 1

soma = 0

while (i <= totalProvas):

	nota = int(input("Digite a nota"))

	soma = soma + nota

	i=i+1 #incremento

print(soma)