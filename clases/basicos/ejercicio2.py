class Distancia:
  def __init__(self, x1=0, y1=0, x2=0, y2=0):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

  def leer_datos(self):
    self.x1= int(input("x1 = "))
    self.y1= int(input("y1 = "))
    self.x2= int(input("x2 = "))
    self.y2= int(input("y2 = "))

  def calcular_distancia(self):
    self.d = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5

  def imprimir_distancia(self):
    print(f"d = {self.d}")