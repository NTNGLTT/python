n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if (n1 < n2) and (n1 < n3):
  print("O menor é ", n1)
elif (n2 < n1) and (n2 < n3):
  print("O menor é ", n2)
else:
  print("O menor é ", n3)