def media(n1,n2,n3):
  soma = n1 + n2 + n3
  return soma/3


num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
num3 = int(input("Num 3: "))

res = media(num1,num2,num3)

print("A media de", num1, num2, num3, "é: ",res)