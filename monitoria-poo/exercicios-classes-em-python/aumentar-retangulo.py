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

  def aumenta(self, outro):
    self.base += outro.base
    self.altura += outro.altura


### Testes
r1 = Retangulo(4, 5)
r2 = Retangulo(1, 2)
r1.aumenta(r2)
assert r1.base == 5 and r1.altura == 7
assert r2.base == 1 and r2.altura == 2