class Tabla(object):
  def leer_datos(self):
    self.n = int(input("Número = "))

  def calcular_tabla(self):
    for i in range(1, 11):
      print(f"{self.n} x {i} = {self.n * i}")