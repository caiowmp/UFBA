from os import sep


class Pessoa:
  def __init__(self, cpf, nome):
    self.cpf = cpf
    self.nome = nome

  def __str__(self):
    return self.nome + " (" + self.cpf + ")"

### Testes
x = Pessoa('111', 'Fulana')
y = Pessoa('222', 'Sicrana')
assert str(x) == 'Fulana (111)'
assert str(y) == 'Sicrana (222)'