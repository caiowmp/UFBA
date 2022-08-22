def retangulo(c, base, altura):
  s =""
  for i in range(altura):
    s += linha(c,base)
    s += "\n"
  return s

def linha(c, n):
  s=""
  for i in range(n):
    s += c
  return s

assert retangulo("*", 4, 2) == "****\n****\n"
assert retangulo("#", 5, 1) == "#####\n"

print(retangulo("*", 4, 2))