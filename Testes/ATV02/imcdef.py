x = int(input("Digite seu peso em KG: "))
y = float(input("Digite sua altura em M: "))


imc = x / (y * y)
imc = round(imc, 2)


def imctext(x):
  if x <= 18.5:
    print("Você está abaixo do peso.")
  if (x > 18.5) and (imc <= 24.9):
    print("Você está com o peso normal.")
  elif (x > 24.9) and (imc <= 29.9):
    print("Você está com sobrepeso.")
  elif x > 29.9:
    print("Você está obeso.")

def main(x):
  imctext(imc)
  
main(imc)