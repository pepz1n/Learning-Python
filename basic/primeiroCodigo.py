import random

pessoas = [
  "Bernardo",
  "Claudio",
  "Mari",
  "Vanessa",
  "Joao",
  "Jonas"
]

bebidas = [
  "cachaça",
  "vodka",
  "whiskey",
  "vinho"
]

lugares = [
  "casa do garbin",
  "casa do pepz",
  "casa da indy",
  "casa de alguem"
]

pessoasDefinitivo = f"{random.choice(pessoas)} e {random.choice(pessoas)}"

print(f"{pessoasDefinitivo} vao pagar a/o {random.choice(bebidas)} na {random.choice(lugares)}")