import math

def distancia(x1, y1, x2, y2):
  '''
  Na aritmética, a divisão euclidiana é o processo de dividir um inteiro por outro, de forma que produza um quociente e um resto menor que o divisor.
  '''
  if x1 > x2:
    x = x1-x2
  else:
    x = x2 - x1

  if y1 > y2:
    y = y1-y2
  else:
    y = y2 - y1

  return math.sqrt(x*x + y*y) 


### Testes
assert distancia(2, 2, 5, 6) == 5
assert distancia.__doc__ is not None