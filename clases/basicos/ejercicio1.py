class Recta:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

  def leer_datos(self):
    self.x1= int(input("x1 = "))
    self.y1= int(input("y1 = "))
    self.x2= int(input("x2 = "))
    self.y2= int(input("y2 = "))

  def calcular_pendiente(self):
    self.m = (self.y2 - self.y1) / (self.x2 - self.x1)

  def imprimir_pendiente(self):
    print(f"m = {self.m}")