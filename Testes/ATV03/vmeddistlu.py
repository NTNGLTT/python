n1 = float(input("Digite o tempo: "))
n2 = float(input("Digite a V media: "))

dist = n1 * n2
lu = dist / 12
lu = round(lu, 2)

print("V med =", n2,"km/h", "Tempo gasto:", n1, "Dist. percorrida: ", dist,"km", "Litros usados: ", lu)