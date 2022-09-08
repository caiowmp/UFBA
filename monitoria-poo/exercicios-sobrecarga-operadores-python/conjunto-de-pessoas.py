class Pessoa:
  def __init__(self, cpf, nome):
    self.cpf = cpf
    self.nome = nome

  def __eq__(self, outro):
    if isinstance(outro, Pessoa) and self.cpf == outro.cpf:
        return True
    else: 
        return False

  def __hash__(self):
    return hash(self.cpf)

### Testes
p1 = Pessoa('111', 'Fulano')
p1x = Pessoa('111', 'Fulanovski')
p3 = Pessoa('333', 'Fulano')
s = set()
s.add(p1)
s.add(p1x)
s.add(p3)
assert len(s) == 2