from os import system


contagem = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
aleatorio = ["Pirata", ["Uma lista dentro da outra", "Socorro"]]

#laço na lista
  
pessoas = []
#append para adicionar a um array
pessoas.append("Bernardo")
pessoas.append("jorjo")
pessoas.append("mateus")
pessoas.append("PEpz")

# print(pessoas)

#remove o ultimo
pessoas.remove("jorjo")

#adiciona em qualquer posicao
pessoas.insert(0, 1)

#tira qualquer posicao
pessoas.pop(0)


# print(pessoas)



numeros = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10]
numeros.append(11)
numeros.append(12)
print(len(numeros))

for numero in numeros:
  print(f"O quadrado de {numero} é:", numero**2)
  

for number in range(1, 11):
  print(f"O quadrado de {number} é:", number**2)
  
system("clear")
print(f"O tamanho de numeros é: {len(numeros)} e seu tipo é {type(numeros)}")