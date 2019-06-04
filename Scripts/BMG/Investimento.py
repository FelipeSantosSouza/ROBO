class Investimento:
  def __init__(self, prazo, dominio, rentabilidade, valorMin, ir, liquidez, tipo):
    self.dominio = dominio
    self.prazo = prazo
    self.tipo = tipo
    self.rentabilidade = rentabilidade
    self.valorMin = valorMin
    self.ir = ir
    self.liquidez = liquidez

  def __str__(self):
    return ''.join([self.tipo, ' - ', self.prazo, ' - ', self.rentabilidade, ' - ', self.ir, ' - ', self.aplicacao_min])
