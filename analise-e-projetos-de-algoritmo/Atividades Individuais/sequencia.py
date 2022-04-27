import numpy as np
import pandas as pd

N = int(input("Informe a quantidade de valores desejados!\n"))
C = int(input("Informe o resultado esperado!\n"))

x = 0
total = 0

while x <= C:
  y = x
  sequence = [y]
  for i in range(N-1): #Cria um array com a sequencia de inteiros do valor X até o Xn
    y += 1
    sequence.append(y)
  x += 1
  sequence = pd.DataFrame(sequence, columns=['Sequence'])
  total = sequence.sum()[0]
  if total == C:
    #print(f"sequence= \n{sequence.transpose().to_string(index=False)}")
    print(f"sequence= \n{sequence.transpose()}")