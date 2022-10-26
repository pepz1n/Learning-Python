[n, l, d] = list(map(int,input().split(" ")))
l *= 1000
totalAluno = n*d
totalTudo = l
while (totalAluno > totalTudo):
  totalTudo += l
print(int(totalTudo/1000))