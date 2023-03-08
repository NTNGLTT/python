nalu = int(input("Digite a quantidade de alunos: "))
cont = 1
nacu = 0

while cont <= nalu:
  n1 = float(input("Digite a nota P1: "))
  n2 = float(input("Digite a nota P2: "))
  cont = cont + 1
  soma = n1 + n2
  media = soma / 2
  nacu = nacu + media
  print("A media é: ", media)
  if media >= 7:
    print("Aluno aprovado direto!")
medgeral = nacu / nalu
print("A media geral é: ", medgeral)