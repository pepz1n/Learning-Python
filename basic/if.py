resposta = input("você quer ouvir uma piada? ")
answerTrue = ["y", "yes"]
answerFalse = ["N", "NO"]


if (resposta.lower() in answerTrue):
  print("sem piada para você")
elif (resposta.upper() in answerFalse):
  print("Tchau!")
else:
  print("Não existe")