def linha(c, n):
  s=""
  for i in range(n):
    s += c
  return s

assert linha("*", 5) == "*****"
assert linha("#", 2) == "##"
assert linha("@", 0) == ""

print(linha("*", 5))