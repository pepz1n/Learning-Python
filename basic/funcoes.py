def oi(nome):
  return f"Oi {nome}!"

print(oi('bernardo'))

def concat(primeiraPalavra, segundaPalavra):
  return primeiraPalavra + " " + segundaPalavra

print(concat('bernardo', 'zanetti'))
print(concat(segundaPalavra='bernardo', primeiraPalavra='zanetti'))


def idadeComoDog(idade):
  return idade * 7

print(idadeComoDog(17))


def maiusculoContrario (palavra):
  return palavra.upper()[::-1]


print(maiusculoContrario("banana"))