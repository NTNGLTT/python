def entrada():
  valor = int(input("Informe um valor inteiro positivo:"))
  if valor < 0:
    print("Valor invalido!")
    valor = int(input("Informe um valor inteiro positivo:"))
    
  return valor

def calculaMedia(x,y,z):
  return(x + y + z) / 3

def main():
  print("Programa para cálculo de média de")
  print("3 valores inteiros positivos")
  n1 = entrada()
  n2 = entrada()
  n3 = entrada()
  print("A media dos valores informados é: ", calculaMedia(n1,n2,n3))

main()