class Investimento:
  def __init__(self, prazo, dominio, rentabilidade, aplicacao_min, ir, liquidez, tipo):
    self.dominio = dominio
    self.prazo = prazo
    self.tipo = tipo
    self.rentabilidade = rentabilidade
    self.aplicacao_min = aplicacao_min
    self.ir = ir
    self.liquidez = liquidez

  def __str__(self):
    return ''.join([self.tipo, ' - ', self.prazo, ' - ', self.rentabilidade, ' - ', self.ir, ' - ', self.aplicacao_min])
