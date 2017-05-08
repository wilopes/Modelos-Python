Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dados = [10, 'a', 3, 8, 9]
>>> dados[0]
10
>>> dados
[10, 'a', 3, 8, 9]
>>> dados.append(3)
>>> dados.insert(0,7)
>>> dados.remove('a')
>>> dados.pop(1)
10
>>> dados.in
SyntaxError: invalid syntax
>>> dados.index(7)
0
>>> dados.count(3)
2
>>> dados
[7, 3, 8, 9, 3]
>>> dados.reverse()
>>> print(dados)
[3, 9, 8, 3, 7]
>>> notas = [10,'a',3,8,9]
>>> notas.append(3)
>>> notas
[10, 'a', 3, 8, 9, 3]
>>> notas.insert(0,7)
>>> notas
[7, 10, 'a', 3, 8, 9, 3]
>>> notas.re
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    notas.re
AttributeError: 'list' object has no attribute 're'
>>> notas.remove('a')
>>> notas
[7, 10, 3, 8, 9, 3]
>>> notas.pop(1)
10
>>> notas
[7, 3, 8, 9, 3]
>>> notas.index(7)
0
>>> notas.count(3)
2
>>> notas.reverse()
>>> notas
[3, 9, 8, 3, 7]
>>> 
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> pro1 = ["maca", 10, 0.30]
>>> pro2 = ["pera", 5, 0.75]
>>> pro3 = ["kiwi", 4, 0.98]
>>> compras = [pro1, pro2, pro3]
>>> compras
[['maca', 10, 0.3], ['pera', 5, 0.75], ['kiwi', 4, 0.98]]
>>> type(compras)
<class 'list'>
>>> type(pro1)
<class 'list'>
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %5.2f" % )e[2]
	
SyntaxError: invalid syntax
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %5.2f" % e[2])

	
Produto: maca
Quantidde: 10
Preco:  0.30
Produto: pera
Quantidde: 5
Preco:  0.75
Produto: kiwi
Quantidde: 4
Preco:  0.98
>>> print("Produto: %s" % e[0])
Produto: kiwi
>>> print("Produto: %s" % e[1])
Produto: 4
>>> print("Produto: %s" % e[2])
Produto: 0.98
>>> produto
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    produto
NameError: name 'produto' is not defined
>>> type(produto)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    type(produto)
NameError: name 'produto' is not defined
>>> print("Produto: %s" % e[0])
print("Quantidde: %d" % e[1])
print("Preco: %5.2f" % e[2])

SyntaxError: multiple statements found while compiling a single statement
>>> 	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %5.2f" % e[2])
	
SyntaxError: unexpected indent
>>> pro1
['maca', 10, 0.3]
>>> pro2
['pera', 5, 0.75]
>>> pro3
['kiwi', 4, 0.98]
>>> compras
[['maca', 10, 0.3], ['pera', 5, 0.75], ['kiwi', 4, 0.98]]
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %5.2f" % e[2])

	
Produto: maca
Quantidde: 10
Preco:  0.30
Produto: pera
Quantidde: 5
Preco:  0.75
Produto: kiwi
Quantidde: 4
Preco:  0.98
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.300000
Produto: pera
Quantidde: 5
Preco: 0.750000
Produto: kiwi
Quantidde: 4
Preco: 0.980000
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %3.2f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.30
Produto: pera
Quantidde: 5
Preco: 0.75
Produto: kiwi
Quantidde: 4
Preco: 0.98
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %2.2f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.30
Produto: pera
Quantidde: 5
Preco: 0.75
Produto: kiwi
Quantidde: 4
Preco: 0.98
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %1.2f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.30
Produto: pera
Quantidde: 5
Preco: 0.75
Produto: kiwi
Quantidde: 4
Preco: 0.98
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.300000
Produto: pera
Quantidde: 5
Preco: 0.750000
Produto: kiwi
Quantidde: 4
Preco: 0.980000
>>> print (preco)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print (preco)
NameError: name 'preco' is not defined
>>> for e in compras:
	print(preco)

	
Traceback (most recent call last):
  File "<pyshell#66>", line 2, in <module>
    print(preco)
NameError: name 'preco' is not defined
>>> for e in compras:
	print(preco[0])

	
Traceback (most recent call last):
  File "<pyshell#68>", line 2, in <module>
    print(preco[0])
NameError: name 'preco' is not defined
>>> for e in compras:
	print(preco e [])
	
SyntaxError: invalid syntax
>>> for e in compras:
	print(preco e [0])
	
SyntaxError: invalid syntax
>>> for e in compras:
	print(e [0])

	
maca
pera
kiwi
>>> for e in compras:
	print(Produtos: %s % e)
	
SyntaxError: invalid syntax
>>> for e in compras:
	print("Produtos: %s" % e)

	
Produtos: ['maca', 10, 0.3]
Produtos: ['pera', 5, 0.75]
Produtos: ['kiwi', 4, 0.98]
>>> for e in compras:
	print("Produtos: %d" % e)

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    print("Produtos: %d" % e)
TypeError: %d format: a number is required, not list
>>> for e in compras:
	print("Produtos: %f" % e)

	
Traceback (most recent call last):
  File "<pyshell#80>", line 2, in <module>
    print("Produtos: %f" % e)
TypeError: must be real number, not list
>>> for e in compras:
	print("Produtos: %s" % e)

	
Produtos: ['maca', 10, 0.3]
Produtos: ['pera', 5, 0.75]
Produtos: ['kiwi', 4, 0.98]
>>> for e in compras:
	print("Produtos: %s" % e[0])

	
Produtos: maca
Produtos: pera
Produtos: kiwi
>>> for e in compras:
	print("Produtos: %s" % e[1])

	
Produtos: 10
Produtos: 5
Produtos: 4
>>> for e in compras:
	print("Produtos: %s" % e[2])

	
Produtos: 0.3
Produtos: 0.75
Produtos: 0.98
>>> for e in compras:
	print("Produtos: %s" % e[3])

	
Traceback (most recent call last):
  File "<pyshell#90>", line 2, in <module>
    print("Produtos: %s" % e[3])
IndexError: list index out of range
>>> for e in compras:
	print("Produtos: %d" % e[0])

	
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    print("Produtos: %d" % e[0])
TypeError: %d format: a number is required, not str
>>> for e in compras:
	print("Produtos: %d" % e[1])

	
Produtos: 10
Produtos: 5
Produtos: 4
>>> produtos
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    produtos
NameError: name 'produtos' is not defined
>>> compras
[['maca', 10, 0.3], ['pera', 5, 0.75], ['kiwi', 4, 0.98]]
>>> for e in compras:
	print("Produtos: %d" % e[2])

	
Produtos: 0
Produtos: 0
Produtos: 0
>>> for e in compras:
	print("Produtos: %f" % e[])
	
SyntaxError: invalid syntax
>>> for e in compras:
	print("Produtos: %f" % e[0])

	
Traceback (most recent call last):
  File "<pyshell#101>", line 2, in <module>
    print("Produtos: %f" % e[0])
TypeError: must be real number, not str
>>> for e in compras:
	print("Produtos: %f" % e[1])

	
Produtos: 10.000000
Produtos: 5.000000
Produtos: 4.000000
>>> for e in compras:
	print("Produtos: %f" % e[2])

	
Produtos: 0.300000
Produtos: 0.750000
Produtos: 0.980000
>>> for e in compras:
	print("Produtos: %2f" % e[2])

	
Produtos: 0.300000
Produtos: 0.750000
Produtos: 0.980000
>>> for e in compras:
	print("Produtos: %2.2f" % e[2])

	
Produtos: 0.30
Produtos: 0.75
Produtos: 0.98
>>> commpras
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    commpras
NameError: name 'commpras' is not defined
>>> compras
[['maca', 10, 0.3], ['pera', 5, 0.75], ['kiwi', 4, 0.98]]
>>> for e in compras:
	print("Produtos: %2.3f" % e[2])

	
Produtos: 0.300
Produtos: 0.750
Produtos: 0.980
>>> for e in compras:
	print("Produtos: %2f" % e[2])

	
Produtos: 0.300000
Produtos: 0.750000
Produtos: 0.980000
>>> for e in compras:
	print("Produtos: %.2f" % e[2])

	
Produtos: 0.30
Produtos: 0.75
Produtos: 0.98
>>> for e in compras:
	print("Produtos: %s" % e)

	
Produtos: ['maca', 10, 0.3]
Produtos: ['pera', 5, 0.75]
Produtos: ['kiwi', 4, 0.98]
>>> compras
[['maca', 10, 0.3], ['pera', 5, 0.75], ['kiwi', 4, 0.98]]
>>> for e in compras:
	print("produto %s" % e [0])

	
produto maca
produto pera
produto kiwi
>>> for e in compras:
	print("produto %d" % e [0])

	
Traceback (most recent call last):
  File "<pyshell#125>", line 2, in <module>
    print("produto %d" % e [0])
TypeError: %d format: a number is required, not str
>>> for e in compras:
	print("produto %d" % e[1])

	
produto 10
produto 5
produto 4
>>> pro1
['maca', 10, 0.3]
>>> pro2
['pera', 5, 0.75]
>>> pro3
['kiwi', 4, 0.98]
>>> print("preco %f")
preco %f
>>> print("preco %f" % [2])
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print("preco %f" % [2])
TypeError: must be real number, not list
>>> print("preco %f" % e[2])
preco 0.980000
>>> print("preco %f" % e[1])
preco 4.000000
>>> print("preco %f" % e[0])
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    print("preco %f" % e[0])
TypeError: must be real number, not str
>>> for e in compras:
	print("Produto: %s" % e[0])
	print("Quantidde: %d" % e[1])
	print("Preco: %f" % e[2])

	
Produto: maca
Quantidde: 10
Preco: 0.300000
Produto: pera
Quantidde: 5
Preco: 0.750000
Produto: kiwi
Quantidde: 4
Preco: 0.980000
>>> 
=============================== RESTART: Shell ===============================
>>> compras
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    compras
NameError: name 'compras' is not defined
>>> compras = []
>>> while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	comprs.append([produto, quntidade, preco])

	
Produto: 
quantidade: 
Traceback (most recent call last):
  File "<pyshell#147>", line 5, in <module>
    quantidade = int(input("quantidade: "))
ValueError: invalid literal for int() with base 10: ''
>>> while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	comprs.append([produto, quntidade, preco])
soma = 0
SyntaxError: invalid syntax
>>> while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	comprs.append([produto, quntidade, preco])
soma = 0
SyntaxError: invalid syntax
>>> while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	comprs.append([produto, quntidade, preco])

	
Produto: while True:
	produto = input("Produto: ")
	if produto == "fim":
		break
	quantidade = int(input("quantidade: "))
	preco = int(input("Preco: "))
	comprs.append([produto, quntidade, preco])
Traceback (most recent call last):
  File "<pyshell#151>", line 2, in <module>
    produto = input("Produto: ")
KeyboardInterrupt
>>> 
 RESTART: C:/Users/Melcrispim/AppData/Local/Programs/Python/Python36-32/InserirItens.py 
Produto: pao
quantidade: 1
Preco: 3
Traceback (most recent call last):
  File "C:/Users/Melcrispim/AppData/Local/Programs/Python/Python36-32/InserirItens.py", line 8, in <module>
    comprs.append([produto, quntidade, preco])
NameError: name 'comprs' is not defined
>>> 
 RESTART: C:/Users/Melcrispim/AppData/Local/Programs/Python/Python36-32/InserirItens.py 
Produto: pao
quantidade: 1
Preco: 50
Traceback (most recent call last):
  File "C:/Users/Melcrispim/AppData/Local/Programs/Python/Python36-32/InserirItens.py", line 8, in <module>
    compras.append([produto, quntidade, preco])
NameError: name 'quntidade' is not defined
>>> 
 RESTART: C:/Users/Melcrispim/AppData/Local/Programs/Python/Python36-32/InserirItens.py 
Produto: pao
quantidade: 1
Preco: 50
Produto: cenoura
quantidade: 2
Preco: 40
Produto: acelga
quantidade: 3
Preco: 60
Produto: fim
pao 1 50 50
cenoura 2 40 80
acelga 3 60 180
Total: 310
>>> compras
[['pao', 1, 50], ['cenoura', 2, 40], ['acelga', 3, 60]]
>>> 
=============================== RESTART: Shell ===============================
>>> lista = [1,7,2,4]
>>> maximo = 1
>>> fir e in lista:
	
SyntaxError: invalid syntax
>>> for e in lista:
	if e > maximo:
		maximo = e

		
>>> for e in lista:
	if e > maximo:
		maximo = e
print(maximo)
SyntaxError: invalid syntax
>>> for e in lista:
	if e > maximo:
		maximo = e
	print(maximo)

	
7
7
7
7
>>> v = [9,8,7,12,0,13,21]
>>> p = []
>>> i = []
>>> for e in v
SyntaxError: invalid syntax
>>> for e in v:
	if e % 2 == 0:
		p.append(e)
	else:
		u.append(e)
	print("pares: ", p)
	print("impares: ", i)

	
Traceback (most recent call last):
  File "<pyshell#175>", line 5, in <module>
    u.append(e)
NameError: name 'u' is not defined
>>> for e in v:
	if e % 2 == 0:
		p.append(e)
	else:
		i.append(e)
	print("pares: ", p)
	print("impares: ", i)

	
pares:  []
impares:  [9]
pares:  [8]
impares:  [9]
pares:  [8]
impares:  [9, 7]
pares:  [8, 12]
impares:  [9, 7]
pares:  [8, 12, 0]
impares:  [9, 7]
pares:  [8, 12, 0]
impares:  [9, 7, 13]
pares:  [8, 12, 0]
impares:  [9, 7, 13, 21]
>>> 
=============================== RESTART: Shell ===============================
>>> 
