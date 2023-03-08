def areatrian(base,alt):
  area = (base * alt) / 2
  return area

def entrada (texto):
  n = int(input(texto))
  return n

def main():
  base = entrada("Digite a base: ")
  alt = entrada("Digite a altura: ")
  area = areatrian(base, alt)
  print("A area é: ",area)

main()