import math
custo = float(input("Digite o custo: "))
ingresso = int(input("Digite o valor do ingresso: "))

ingressocusto = math.ceil (custo / ingresso)
custolucro = custo + (custo * 0.23)
lucro = math.ceil (custolucro / ingresso)

print("Devem ser vendidos", ingressocusto, "para que o valor de custo seja alcançado.")
print("Para que se tenha um lucro de 23% é necessario vender", lucro,"ingressos.")
