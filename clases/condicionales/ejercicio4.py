class Calculo(object):
  def leer_datos(self):
    self.x_centro = int(input("x centro: "))
    self.y_centro = int(input("y centro: "))
    self.radio = int(input("radio: "))
    self.x_punto = int(input("x punto: "))
    self.y_punto = int(input("y punto: "))

  def calcular(self):
    self.distancia = ((self.x_punto - self.x_centro)**2 + (self.y_punto - self.y_centro)**2)**0.5
    if self.distancia > self.radio:
      self.punto = "El punto está fuera de la circunferencia"
    if self.distancia < self.radio:
      self.punto = "El punto está dentro de la circunferencia"
    if self.distancia == self.radio:
      self.punto = "El punto está sobre la circunferencia"

  def imprimir(self):
    print(self.punto)