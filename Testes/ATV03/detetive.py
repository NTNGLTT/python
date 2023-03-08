p1 = input("Telefonou para a vitima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Morava perto da vitima? ")
p4 = input("Devia para a vitima? ")
p5 = input("Ja trabalhou com a vitima? ")

susp = 0

if (p1 == "sim"):
  susp=susp + 1
if (p2 == "sim"):
  susp=susp + 1
if (p3 == "sim"):
  susp=susp + 1
if (p4 == "sim"):
  susp=susp + 1
if (p5 == "sim"):
  susp=susp + 1

if susp == 2:
  print("Você é suspeito!")
elif (susp >= 3) and (susp <= 4):
  print("Você é cúmplice!")
elif (susp == 5):
  print("Você é o Assassino!")
else:
  print("Você é inocente.")