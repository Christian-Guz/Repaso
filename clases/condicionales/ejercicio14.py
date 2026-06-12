class Numero(object):
  def __init__(self):
    self.numero = 0
    self.x = ""
    
  def leer_datos(self):
    self.numero = int(input("Número = "))

  def imprimir_numero(self):
    if self.numero < 2:
      self.x = "No es un número primo"
      return
    for i in range(2, self.numero):
      if self.numero % i == 0:
        self.x = "No es un número primo"
        return
    self.x = "Es un número primo"
    print(self.x)