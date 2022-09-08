class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    @property
    def valor_decimal(self):
        return self.numerador / self.denominador

    def __str__(self):
        return str(self.numerador) +'/'+ str(self.denominador)

    def __eq__(self,outro):
        if isinstance(outro, Fracao):
            return self.numerador/self.denominador == outro.numerador/outro.denominador
        return False

    def __lt__(self, outro):
       if isinstance(outro, Fracao):
           return self.numerador/self.denominador < outro.numerador/outro.denominador
       return NotImplemented



### Testes
f1_2 = Fracao(1, 2)
f3_6 = Fracao(3, 6)
f3_4 = Fracao(3, 4)
assert f1_2 == f3_6
assert f3_6 != f3_4
assert str(f1_2) == '1/2'
assert str(f3_6) == '3/6'
l = [f1_2, f3_4, f3_6]
assert sorted(l)[2] == f3_4