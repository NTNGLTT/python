import math
A = float(input("Digite o lado: "))
B = float(input("Digite o lado: "))

aquad = math.pow(A,2)
bquad = math.pow(B,2)
hipo = aquad + bquad
nusa = math.sqrt(hipo)

print("Os valores ao elevados ao quadrado são: ", aquad, bquad)
print("A hipotenusa é: ", nusa)