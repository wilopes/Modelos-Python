temFilho = input("Vc tem filho S ou N \n")
while (temFilho == "S"):
  try:
      numeFilho = int(input("Nume Filhos: "))
      break
  except:
    print("Vc tem que digitar valor nume")
