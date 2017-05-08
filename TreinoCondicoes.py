nome = input("Digite seu nome: ")
#Digite seu nome: 
print("Seu nome e %s"%(nome))
#Seu nome e 
nome = input("Digite seu nome: ")
#Digite seu nome: Wilton Lopes
print("Seu nome e %s"%(nome))
#Seu nome e Wilton Lopes
type(nome)
<class 'str'>
email = input("Digite seu email: ")
Digite seu email: 
print(email)

email = input("Digite seu email: ")
Digite seu email: wlopes@mtzol.com.br
print(email)
wlopes@mtzol.com.br

salario = input("Digite seu salario: ")
Digite seu salario: 100.00
print(salario)
100.00
type(salario)
<class 'str'>
descontos
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    descontos
NameError: name 'descontos' is not defined
DESCONTOS = 100.00
GRATIFICACAO = 50.00
SalarioNovo = salario + GRATIFICACAO - DESCONTOS
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    SalarioNovo = salario + GRATIFICACAO - DESCONTOS
TypeError: must be str, not float
type(salario)
<class 'str'>
salario = float(salario)
SalarioNovo = salario + GRATIFICACAO - DESCONTOS
salarionovo
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    salarionovo
NameError: name 'salarionovo' is not defined
SalarioNovo
50.0
salario = input("Digite seu salario: ")
Digite seu salario: 500.00
salario
'500.00'
SalarioNovo = salario + GRATIFICACAO - DESCONTOS
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    SalarioNovo = salario + GRATIFICACAO - DESCONTOS
TypeError: must be str, not float
type(salario)
<class 'str'>
salario = float(salario)
SalarioNovo = salario + GRATIFICACAO - DESCONTOS
salario
500.0
SalarioNovo = salario + GRATIFICACAO - DESCONTOS
salario
500.0
DESCONTOS
100.0
GRATIFICACAO
50.0
SalarioNovo
450.0

=============================== RESTART: Shell ===============================
SalarioNovo
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    SalarioNovo
NameError: name 'SalarioNovo' is not defined
nome = "Wilton Lopes"
salario = 600.00
salario = salario + 50.00
salario = salario - 200.00
salario = salario*2
salario
900.0
salario = salario**2
salario
810000.0
salario = input("Digite seu salario: ")
Digite seu salario: 400
salario
'400'
salario = input("Digite seu salario: ")
Digite seu salario: 400.00
salario
'400.00'
salario = float(input("Digite seu salario: "))
Digite seu salario: 800
salario
800.0
salario == 500.00
False
salario != 300.00
True
salario > 900.00
False
salario <= 1000.00
True
salario
800.0

=============================== RESTART: Shell ===============================
nome = input("Digite seu nome: ")
Digite seu nome: wilton lopes
print(nome)
wilton lopes
(nome == "wilton lopes") and (salario > 400.00)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    (nome == "wilton lopes") and (salario > 400.00)
NameError: name 'salario' is not defined
salario  = 800.00
(nome == "wilton lopes") and (salario > 400.00)
True
(nome == "samara") and (salario > 400.00)
False
((nome == "samara") and (salario < 400.00)) or (nome != "andre")
True
((nome == "samara") and (salario - DESCONTOS) < 900.00)
False
DESCONTOS = 100.00
((nome == "samara") and (salario - DESCONTOS) < 900.00)
False

=============================== RESTART: Shell ===============================
SalarioMinimo = 880.00

============ RESTART: C:/Users/Melcrispim/Downloads/condicoes.py ============
Digite seu salario: 600.00
Voce tem filho? S - sim ou N - nao 
S
Digite o numero de filhos: 2
Traceback (most recent call last):
  File "C:/Users/Melcrispim/Downloads/condicoes.py", line 7, in <module>
    salario = salariMinimo + (ajudaFilho * numeroFilhos)
NameError: name 'salariMinimo' is not defined

============ RESTART: C:/Users/Melcrispim/Downloads/condicoes.py ============
Digite seu salario: 600.00
Voce tem filho? S - sim ou N - nao 
S
Digite o numero de filhos: 2
920.0

============ RESTART: C:/Users/Melcrispim/Downloads/condicoes.py ============
Digite seu salario: 1200
Voce tem filho? S - sim ou N - nao 
n
Digite o numero de filhos: 0
880.0

============ RESTART: C:/Users/Melcrispim/Downloads/condicoes.py ============
Digite seu salario: 1200
Voce tem filho? S - sim ou N - nao 
s
Digite o numero de filhos: 2
920.0

============ RESTART: C:/Users/Melcrispim/Downloads/condicoes.py ============
Digite seu salario: 1200.00
Voce tem filho? S - sim ou N - nao 
S
Digite o numero de filhos: 1
900.0

