cont = 0
maior = 0
menor = 0
sef = 0
veio = 0

while cont >= 0:
  id = int(input("Idades: ")) 
  cont = cont + 1
  if id < 0:
    break
  se = input("Sexo (M/F): ")

  if cont == 1:
    maior = id
    menor = id
  else:
    if id > maior:
      maior = id
    if id < menor:
      menor = id
      
  if cont > 1:    
    if se == "F" and id >= 18 and id <= 35:
        sef = sef + 1    
  porc = (sef * 100) / cont

  if cont > 1:
    if id >= 65:
      veio = veio + 1
  porcv = (veio * 100) / cont


print("A maior idade é:", maior)
print("A menor idade é:", menor)
print("O percentual de mulheres entre 18 e 35 anos é:", porc,"%")
print("O percentual de pessoas com idade maior ou igual a 65 é:", porcv)