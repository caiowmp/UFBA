def maior(lista):
  if len(lista) == 0:
    return 0
  else:
    lista1 = []
    for i in lista:
      lista1.append(i)
    lista1.sort()
    lista1.reverse()
    return lista1[0]

def media_justa(lista):
  tam = len(lista) - 1
  if tam < 1:
    return 0
  else:
    soma = 0
    for i in lista:  
      soma += int(i)
    soma -= int(maior(lista))
    return soma/tam

### Testes
assert maior([]) == 0
assert maior([4]) == 4
assert maior([3, 5, 2]) == 5
assert maior([8, 3, 5, 2]) == 8
assert maior([8, 3, 5, 9]) == 9

assert media_justa([]) == 0
assert media_justa([6]) == 0
assert media_justa([12, 18]) == 12
assert media_justa([1, 3, 5]) == 2

# a lista não deve ser modificada
l = [1, 3, 5]
lcopy = l.copy()
media_justa(l)
assert l == lcopy

from unittest.mock import MagicMock
maior = MagicMock(return_value=5)
assert media_justa([5, 10]) == 10
maior.assert_called()