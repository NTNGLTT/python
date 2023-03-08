tempo = int(input("Digite a duração em segundos: "))

hora = tempo // 3600
tempo = tempo % 3600
minuto = tempo // 60
segundo = tempo % 60

print (hora,"h", minuto, "m", segundo, "s")