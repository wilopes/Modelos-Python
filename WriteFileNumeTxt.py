'''
arquivo = open("nume.txt", "a")
for linha in range(1,101):
    arquivo.write("%d\n" % linha)
arquivo.close()
'''
arquivo = open("nume.txt","r")
lista = arquivo.readlines()
for posicao in lista:
    print(posicao)
arquivo.close()
