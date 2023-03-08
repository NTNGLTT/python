x = float(input("Digite o raio do circulo: "))
pi = 3.14

def areacirc ():
  area = pi * (x ** 2)
  return area

def pericirc ():
  peri = (2 * pi) * x
  return peri

def main (x):
    print("A area é: ",areacirc(),"e o perimetro: ",pericirc())

main (x)