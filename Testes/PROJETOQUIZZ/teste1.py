placar = 0
qtdcerto = 0


print("No dia 16 de março é celebrado o Dia Nacional da Conscientização sobre as Mudanças Climáticas. A data chama a atenção da população para essa questão e também para a necessidade de ações que reduzam o impacto dessas mudanças sobre a Terra.")

print("1. Qual o principal fenômeno que promove as mudanças climáticas no planeta Terra?")

print("A-) Nenhum fenômeno provoca mudanças climáticas.")
print("B-) O efeito estufa provoca apenas o aquecimento do oceano Índico.")
print("C-) O efeito estufa que provoca o esfriamento da Terra.")
print("D-) O efeito estufa que provoca o aquecimento global.")
print("E-) A poluição é a responsável pelas mudanças climáticas.")
q1 = input("Digite sua resposta: ")
if q1 == "D":
  print("Parabéns, essa é a resposta correta! O maior causador dos fenômenos climáticos na Terra é o efeito estufa, que provoca o aquecimento global. ")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, o grande responsável pelas mudanças climáticas na Terra é o efeito estufa, sendo ele quem provoca o aquecimento global. ")
  placar = placar - 20

print("2. O que é o aquecimento global? ")

print("A-) É a baixa temperatura que prejudica o planeta Terra. ")
print("B-) É o aumento da temperatura do planeta Terra. ")
print("C-) É quando o Sol está próximo do planeta Terra.")
print("D-) É o aumento da temperatura do planeta Marte.")
print("E-) É quando chegamos na estação do verão. ")
q2 = input("Digite sua resposta: ")
if q2 == "B":
  print("Parabéns, essa é a resposta correta! O aquecimento global se dá ao aumento da temperatura do planeta Terra.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, o aquecimento global é o aumento da temperatura do planeta Terra.")
  placar = placar - 20

print("3. Quais ações humanas descritas, provocam a maior produção de gases na atmosfera? ")

print("A-) Jogar lixo no rio.")
print("B-) Todas as respostas.")
print("B-) Todas as respostas.")
print("D-) Queima de madeira, combustão da gasolina e materiais nas indústrias.")
print("E-) Poluição dos rios.")
q3 = input("Digite sua resposta: ")
if q3 == "D":
  print("Parabéns, essa é a resposta correta! A queima de madeira, combustão da gasolina e materiais nas indústrias é a principal causa da produção de gases na atmosfera.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, a maior causadora da produção de gases na atmosfera é a queima de madeira, combustão da gasolina e materiais nas indústrias.")
  placar = placar - 20

print("4. O que é o efeito estufa? Ele é prejudicial ou não? ")

print("A-) Um fenômeno natural que ocorre a partir da concentração de gases na atmosfera que formam uma camada bloqueando a volta de raios UV. Em excesso ele é prejudicial.")
print("B-) Um nome derivado ao aquecimento global.")
print("C-) Efeito estufa é um fenômeno natural derivado dos gases na atmosfera e não é prejudicial.")
print("D-) Não é prejudicial.")
print("E-) É prejudicial.")
q4 = input("Digite sua resposta: ")
if q4 == "A":
  print("Parabéns, essa é a resposta correta! O efeito estufa é uma consequência do aquecimento global, assim sendo prejudicial é um fenômeno natural que ocorre a partir da concentração de gases na atmosfera que formam uma camada que bloqueia a volta de raios UV logo aquece o planeta.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, o efeito estufa é uma consequência do aquecimento global, assim sendo prejudicial é um fenômeno natural que ocorre a partir da concentração de gases na atmosfera que formam uma camada que bloqueia a volta de raios UV logo aquece o planeta.")
  placar = placar - 20

print("5. As mudanças climáticas estão ocorrendo e já é possível notar algumas modificações que provavelmente relacionam-se com a ação do homem. Assim sendo, são necessárias ações urgentes para que nosso impacto no meio ambiente seja reduzido. Analise as alternativas abaixo e marque aquela que não indica uma forma de deter o avanço das mudanças climáticas.")

print("A-) Realizar técnicas na agricultura que evitam a emissão de carbono.")
print("B-) Criar programas de reflorestamento, principalmente em áreas urbanas.")
print("C-) Aumentar o uso de combustíveis fósseis.")
print("D-) Realizar frequentemente a regulagem dos carros.")
print("E-) Realizar consumo consciente.")
q5 = input("Digite sua resposta: ")
if q5 == "C":
  print("Parabéns, essa é a resposta correta! A queima de combustíveis fósseis causa a produção de gases que intensificam o efeito estufa, sendo uma maneira, portanto, de acelerar as mudanças climáticas.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, o que agravaria as mudanças climáticas seria aumentar o uso de combustíveis fósseis, que geraria mais gases e aumentaria ainda mais o efeito estufa.")
  placar = placar - 20

print("6. Muitas pessoas acreditam que as mudanças climáticas afetam exclusivamente a temperatura do planeta, que se torna mais quente. Entretanto, muitas vezes, essas pessoas esquecem que, ao aumentar a temperatura, uma série de organismos e ecossistemas são gravemente afetados. Observe as alternativas abaixo e marque a única que não é uma consequência da alteração da temperatura do planeta. ")

print("A-) Diminuição da biodiversidade.")
print("B-) Alterações do regime de chuvas.")
print("C-) Secas prolongadas.")
print("D-) Aumento da frequência de terremotos.")
print("E-) Aumento de doenças respiratórias.")
q6 = input("Digite sua resposta: ")
if q6 == "D":
  print("Parabéns, essa é a resposta correta! Os terremotos ocorrem por causa de movimentações das placas tectônicas, não havendo ligação, portanto, com o aumento da temperatura.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, seria o aumento da frequência de terremotos. Porque o aumento da temperatura não interfere no movimento das placas tectônicas.")
  placar = placar - 20

print("7. Cientistas acreditam que o reflorestamento e o plantio de árvores em áreas sem vegetação podem contribuir para minimizar o aquecimento global. A redução desse aquecimento ocorreria porque: ")

print("A-) Diminuiria a quantidade de dióxido de carbono na atmosfera, que seria utilizado pela fotossíntese.")
print("B-) Aumentaria a quantidade de dióxido de carbono na atmosfera, liberado pela respiração celular.")
print("C-) A expansão das florestas seria inibida, em longo prazo, pelo excesso de gás carbônico liberado.")
print("D-) Diminuiria o efeito estufa, com a liberação de gás carbônico, em decorrência da expansão da cobertura vegetal.")
print("E-) A evaporação da agua nas arvores contribuiria para o equilibrio de umidade e carbono.")
q7 = input("Digite sua resposta: ")
if q7 == "A":
  print("Parabéns, essa é a resposta correta! Diminuiria a quantidade de dióxido de carbono na atmosfera, que sería utilizado como alimento das plantas para a realização da fotossíntese.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, diminuiria a quantidade de dióxido de carbono na atmosfera, que sería utilizado pela fotossíntese.")
  placar = placar - 20

print("8. Assinale a alternativa que NÃO APRESENTA uma consequência do aquecimento global:")

print("A-) Derretimento das geleiras, nos extremos da Terra.")
print("B-) Desflorestamento e queimadas das áreas de matas.")
print("C-) Secas severas, que causam maior escassez de água.")
print("D-) Aumento do nível do mar, causando inundações costeiras.")
print("E-) Tempestades mais severas.")
q8 = input("Digite sua resposta: ")
if q8 == "B":
  print("Parabéns, essa é a resposta correta! Desflorestamento e queimadas das áreas de matas é uma das causas do aquecimento global, não consequência.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade, esta é de fato uma consequência do aquecimento global, já o desflorestamento e queimadas das áreas de matas é uma causa do mesmo.")
  placar = placar - 20

print("9. Nos últimos anos, observa-se um aumento crescente do percentual de CO2 na atmosfera. Entre outros efeitos, o excesso de CO2 pode contribuir para:")

print("A-) Resfriamento global.")
print("B-) Diminuição da fotossíntese.")
print("C-) Aumento da camada de ozônio.")
print("D-) Aquecimento global.")
print("E-) Diminuição da camada de ozônio.")
q9 = input("Digite sua resposta: ")
if q9 == "D":
  print("Parabéns, essa é a resposta correta! O excesso pode contribuir para o aquecimento global.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade,  excesso pode contribuir para o aquecimento global.")
  placar = placar - 20

print("10. Sobre o aquecimento global, que é o processo de elevação das temperaturas médias da Terra ao longo do tempo, marque a alternativa correta.")

print("A-) É causado pela falta de saneamento básico e pela poluição dos rios e mares.")
print("B-) São consequências do aquecimento global: diminuição do nível da água dos oceanos e um maior congelamento das calotas polares.")
print("C-) Tem como causa principal a emissão de poluentes para a atmosfera dos chamados gases-estufa. Os gases-estufa mais conhecidos são o dióxido de carbono e o gás metano.")
print("D-) São consequências do aquecimento global: furacões no Nordeste brasileiro e aumento do nível das águas dos rios da Amazônia.")
print("E-) A poluição das atividades industriais e as queimadas de florestas não têm nenhuma relação com o aquecimento global.")
q10 = input("Digite sua resposta: ")
if q10 == "C":
  print("Parabéns, essa é a resposta correta! O efeito estufa tem como causa principal a emissão de poluentes para a atmosfera dos chamados gases-estufa. Os gases-estufa mais conhecidos são o dióxido de carbono e o gás metano.")
  placar = placar + 50
  qtdcerto = qtdcerto + 1
else:
  print("Resposta incorreta! Na verdade a elevação média das temperaturas se dá principalmente pela emissão de gases poluentes que interferem na volta dos raios UV para a estratosfera.")
  placar = placar - 20

print("Quantidade de Acertos: "qtdcerto,"/10")
print("Pontuação: "placar,"/500")

if placar > 350:
  print("Parabéns!!! Você é Crânio!")
elif placar > 250:
  print("Parabéns!! Você foi Excelente!")
else:
  print("Parabéns! Você foi Bom!"),
  