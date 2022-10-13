import os

value = float((input("Quanto a janta custou? ")).replace("R$", ''))
tip = int(input("Qual a gorjeta?\n1- 15%;\n2- 18%;\n3- 20%.\n"))
gorjeta = 0

match tip:
  case 1:
    gorjeta = value*(15/100)

  case 2:
    gorjeta = value * (18/100)
  
  case 3:
    gorjeta = value * (20/100)
  
  case _:
    print("Sem gorjeta")

os.system("clear")
print(f"A janta custou: R$ {value:.2f}")
print(f"A gorjeta custou: R$ {gorjeta:.2f}")
print(f"O total foi: R$ {(gorjeta + value):.2f}")
