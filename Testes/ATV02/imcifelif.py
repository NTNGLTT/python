n1 = int(input("Digite seu peso em KG: "))
n2 = float(input("Digite sua altura em M: "))

imc = n1 / (n2 * n2)
imc = round(imc, 2 )
print("IMC= ", imc)

if imc <= 18.5:
  print("Você está abaixo do peso.")
if (imc > 18.5) and (imc <= 24.9):
  print("Você está com o peso normal.")
elif (imc > 24.9) and (imc <= 29.9):
  print("Você está com sobrepeso.")
elif imc > 29.9:
  print("Você está obeso.")