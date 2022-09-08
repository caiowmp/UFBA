class Pessoa:
  def __init__(self, cpf, nome):
    self.cpf = cpf
    self.nome = nome

  def __eq__(self, outro):
    if isinstance(outro, Pessoa) and self.cpf == outro.cpf:
        return True
    else: 
        return False

### Testes
p1 = Pessoa('111', 'Fulano')
p1x = Pessoa('111', 'Fulanovski')
p2 = Pessoa('222', 'Sicrana')
p3 = Pessoa('333', 'Fulano')
assert p1 == p1 and p2 == p2 and p3 == p3
assert p1 == p1x
assert p1 != p2 and p1 != p3
assert p1 != 'Fulano'
assert p1 != None