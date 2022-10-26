a = int(input())

for i in range(a):
  aluno = input()
  valores = list(map(float,input().split(" ")))
  valores.sort(reverse=True)
  if (len(valores) == 4):
    valores.pop()
  total = 0
  for i in valores:
    total += i
  if (len(valores) == 3):
    print(f"{aluno}: {(total/3):.2}")
  else:
    print(f"{aluno}: {(total/2):.2}")
