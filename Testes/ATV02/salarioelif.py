n1 = int(input("Digite o número de horas: "))
n2 = int(input("Digite o valor de cada hora: "))

st = n1 * n2

if n1 > 200:
  print("O salário com acréscimo é: ", st + 1000)
elif (n1 >= 160) and (n1 <= 200):
  print("O salário com acréscimo é: ", st + 500)
else:
  print("O salário é: ", st, "sem acréscimo.")

if n1 >= 200:
  print("Seu rendimento foi ótimo")
elif (n1 >= 160) and (n1 < 200):
  print("Seu rendimento foi muito bom")
else:
  print("Seu rendimento foi bom")