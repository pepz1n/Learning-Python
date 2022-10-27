a = int(input())

for i in range(a):
  [minutos, tempo] = list(map(lambda a: int(a.replace("T", "")) ,input().split(" ")))
  if(minutos > 45):
    if (tempo == 1):
      print(f"{45}+{minutos-45}")  
    else:
      print(f"{90}+{minutos-45}")
  else:
    if (tempo == 1):
      print(minutos)  
    else:
      print(minutos+45)
      