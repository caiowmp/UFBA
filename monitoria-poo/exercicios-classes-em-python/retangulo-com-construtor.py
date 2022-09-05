class Retangulo:
  
  def __init__(self, b, a):
    self.base = b
    self.altura = a

  def altera_dimensoes(self, b, a):
    self.base = b
    self.altura = a
  def area(self):
    return self.base * self.altura
  def perimetro(self):
    return 2*(self.base + self.altura)

### Testes
r = Retangulo(3, 4)
assert r.area() == 12
r.base = 5
assert r.area() == 20