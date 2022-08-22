def sequencia(n):
  if n == 0:
    return []
  else:
    resposta = []
    for i in range(1,n+1):
      resposta.append(i)
    return resposta
  
assert sequencia(3) == [1, 2, 3]
assert sequencia(1) == [1]
assert sequencia(-1) == []

print(sequencia(3))