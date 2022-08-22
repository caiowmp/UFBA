def produtorio(lista):
  resultado = 1
  if len(lista) == 0:
  	return resultado
  else:
    for i in lista:
      resultado *= i
  return resultado

assert produtorio([]) == 1
assert produtorio([1, 2, 3]) == 6
assert produtorio([1, 0, 3]) == 0

print(produtorio([1, 2, 3]))