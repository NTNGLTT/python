codr = input("Digite o codigo de região do cliente (1, 2, 3, 4): ")
nome = input("Digite o nome do cliente: ")
npç = int(input("Digite o numero de peças vendidas: "))
nomev = input("Digite o nome do vendedor: ")

custopç = 7
if npç <= 1000:
  if codr == "1":
    custopç = custopç + 1
  if codr == "2":
    custopç = custopç + 1.1
  if codr == "3":
    custopç = custopç + 1.15
  if codr == "4":
    custopç = custopç + 1.2
elif npç > 1000:
  if codr == "1":
    custopç = custopç + 0.9
  if codr == "2":
    custopç = custopç + 1
  if codr == "3":
    custopç = custopç + 1.1
  if codr == "4":
    custopç = custopç + 1.15
    
custot = custopç * npç
print("O valor do frete é: ", custot)

valort = custot + (custot * 0.50)
comiv = valort * 0.065
print("A comissão é: ", comiv)

lucro = valort - custot - comiv
print("O lucro é: ", lucro)