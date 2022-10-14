import math

[nota1, nota2, nota3, nota4] =list(map(float,input().split(" ")))

media = (nota1*0.2) + (nota2*0.3) + (nota3*0.4) + (nota4*0.1)
media = math.floor(media*100)/100

print(f"Media: {round(media, 1)}")

if (media >= 7):
  print("Aluno aprovado.")
elif (media < 5):
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  
  notaExame = float(input())
  print(f"Nota do exame: {notaExame:.1f}")
  media += notaExame
  media /= 2
  media = math.floor(media*100)/100
  print("Aluno aprovado." if media > 4.9 else "aluno reprovado.")
  print(f"Media final: {media:.1f}")