def faixa_etaria(idade):
  if idade <=1:
  	return "bebê"
  elif idade <=11:
    return "criança"
  elif idade <=17:
    return "adolescente"
  else:
    return "adulta"

assert faixa_etaria(0) == "bebê"
assert faixa_etaria(1) == "bebê"
assert faixa_etaria(2) == "criança"
assert faixa_etaria(11) == "criança"
assert faixa_etaria(12) == "adolescente"
assert faixa_etaria(17) == "adolescente"
assert faixa_etaria(18) == "adulta"
assert faixa_etaria(81) == "adulta"


x = int(input())
print(faixa_etaria(x))