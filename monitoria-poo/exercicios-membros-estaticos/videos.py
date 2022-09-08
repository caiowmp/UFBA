class Video:

  TIPO_FILME = "filme"
  TIPO_SERIE = "serie"

  def __init__(self, id, tipo):
    self.id = id
    self.tipo = tipo
	
  @classmethod
  def tipos(cls):
    retorno = []
    retorno.append(cls.TIPO_FILME)
    retorno.append(cls.TIPO_SERIE)
    return retorno
    
### Testes
print(Video.tipos())
assert Video.TIPO_FILME == 'filme'
assert Video.TIPO_SERIE == 'serie'
assert Video.tipos() == ['filme', 'serie']
print(Video.TIPO_FILME)
print(Video.TIPO_SERIE)
Video.TIPO_FILME = 'f'
Video.TIPO_SERIE = 's'  
assert Video.tipos() == ['f', 's']
print(Video.TIPO_FILME)
print(Video.TIPO_SERIE)

'''
No teste, sempre que chamar o método tipos, tem que ser Video.tipos()
'''