from time import time


a = int(input())
start = time()
for i in range(a):
  cartasUsuario = int(input())
  for altura in range(1, cartasUsuario):
    totalCartas = (3*(altura*(altura-1))/2)+altura*2
    if(cartasUsuario - totalCartas < 0 ):
      print(altura-1)
      break 
    elif (cartasUsuario - totalCartas == 0 ):
      print(altura)
      break
  totalCartasFim = (altura)
  
end = time()

print(f"tempo: {end-start}")