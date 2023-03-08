cont = 0
maior = 0
menor = 0

while cont >= 0:
  n = int(input("Digite uma sequencia de numeros: "))
  cont = cont + 1
  if n < 0:
    break
    
  if cont == 1:
    maior = n
    menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
      
print("O maior numero é:", maior)
print("O menor numero é:", menor)