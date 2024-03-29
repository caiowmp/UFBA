class Conta:  
  def __init__ (self,codigo, saldo = 0):
    self.saldo = saldo
    self.codigo = codigo
  
  def deposita(self, quantia):
    self.saldo += quantia
  
  def retira(self, quantia):
    if self.saldo > quantia:
        self.saldo -= quantia
        return True
    else:
        return False
  
  def transfere(self, quantia, beneficiario):
    if self.saldo > quantia and beneficiario != None:
        self.retira(quantia)
        beneficiario.deposita(quantia)
        return True
    else:
        return False

### Testes
import unittest
class TestConta(unittest.TestCase):
  def test_cria_conta_sem_informar_saldo(self):
    c = Conta('123')
    self.assertEqual(c.codigo, '123')
    self.assertEqual(c.saldo, 0)

#  def test_nao_pode_alterar_codigo(self):
#    c = Conta('123', 50.0)
#    with self.assertRaises(AttributeError):
#        c.codigo = '456'

#  def test_nao_pode_alterar_saldo(self):
#    c = Conta('123', 50.0)
#    with self.assertRaises(AttributeError)
#        c.saldo = 999.99

  def test_cria_conta_com_saldo(self):
    c = Conta('123', 50)
    self.assertEqual(c.saldo, 50)
  
  def test_retira_com_saldo_suficiente(self):
    c = Conta('123', 100.0)
    self.assertTrue(c.retira(40.0))
    self.assertAlmostEqual(c.saldo, 60.0)
  
  def test_retira_com_saldo_insuficiente(self):
    c = Conta('123', 30.0)
    self.assertFalse(c.retira(40.0))
    self.assertAlmostEqual(c.saldo, 30.0)

  def test_deposita(self):
    c = Conta('123', 50.0)
    c.deposita(40.0)
    c.deposita(10.5)
    self.assertAlmostEqual(c.saldo, 100.5)
  
  def test_transfere_com_saldo_suficiente(self):
    conta = Conta("123", 50.0)
    beneficiario = Conta("999", 10.0)
    
    self.assertTrue(conta.transfere(30.0, beneficiario))
    self.assertAlmostEqual(40.0, beneficiario.saldo)
    self.assertAlmostEqual(20.0, conta.saldo)

  def test_transfere_com_saldo_insuficiente(self):
    conta = Conta("123", 5.0)
    beneficiario = Conta("999", 10.0)
    
    self.assertFalse(conta.transfere(30.0, beneficiario))
    self.assertAlmostEqual(10.0, beneficiario.saldo)
    self.assertAlmostEqual(5.0, conta.saldo)

  
  def test_transfere_para_beneficiario_inexistente(self):
    conta = Conta("123", 5.0)
    beneficiario = None
    
    self.assertFalse(conta.transfere(2.0, beneficiario))
    self.assertAlmostEqual(5.0, conta.saldo)

if __name__ == '__main__':
  import sys
  unittest.main(exit=False)