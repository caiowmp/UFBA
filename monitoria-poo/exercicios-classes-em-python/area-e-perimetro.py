class Retangulo:
  
  def __init__(self):
    self.base = 0
    self.altura = 0

  def altera_dimensoes(self, b, a):
    self.base = b
    self.altura = a
  def area(self):
    return self.base * self.altura
  def perimetro(self):
    return 2*(self.base + self.altura)


### Testes
r = Retangulo()
r.base = 4
r.altura = 3
assert r.area() == 12
assert r.perimetro() == 14
r.base = 5
assert r.area() == 15
assert r.perimetro() == 16