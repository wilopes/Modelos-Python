i = 1

while i<=3:

    aluno = input('Digite o nome do aluno')

   

    nota1 = float(input('Digite a nota da prova 1 do aluno'))

    nota2 = float(input('Digite a nota da prova 2 do aluno'))

    media = (nota1 + nota2 )/ 2

    if (media >= 7):

        print('Aprovado')

    else:

        print('Reprovado')

    i = i +1
