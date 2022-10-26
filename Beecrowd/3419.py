[pilotos, voltas] = list(map(int,input().split(" ")))

pilotoRapido = 0
posicaoI = 0
total = 0
voltaMaisRapida = 9999999
for i in range(1, pilotos+1):
  corredor = list(map(lambda a: int(a.replace(":", "")) ,input().split(" ")))
  pilotoAtual = corredor[0]
  corredor.pop(0)
  todasVolta = 0
  for j in corredor:
    todasVolta += j
    if(j < voltaMaisRapida):
      pilotoRapido = pilotoAtual
      voltaMaisRapida = j
      posicaoI = i
      total = todasVolta
    elif (j == voltaMaisRapida ):
      if (todasVolta < total):
        pilotoRapido = pilotoAtual
        voltaMaisRapida = j
        posicaoI = i
        total = todasVolta
      
      


print(pilotoRapido if i <=10 else "NENHUM")