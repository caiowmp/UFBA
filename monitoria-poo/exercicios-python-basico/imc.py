def esta_obesa(peso, altura):
  imc = peso/(altura**2)
  
  if imc >= 30 :
    return True
  else:
    return False

assert esta_obesa(70, 1.70) == False
assert esta_obesa(170, 1.70) == True