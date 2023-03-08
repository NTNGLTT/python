soma = 0

while True:
  v = int(input("Digite o numero para somar (Digite 0 para sair): "))
  if v == 0:
    break
  soma = soma + v
print("Soma =", soma)