class Inversion(object):
  def leer_datos(self):
    self.cantidad = float(input("Cantidad a invertir = "))
    self.interes = float(input("Interés anual = "))
    self.años = int(input("Número de años = "))
    self.interes /= 100

  def calcular_inversion(self):
    for i in range(1, self.años + 1):
      self.cantidad *= (1 + self.interes)
      print(f"Año {i}: {self.cantidad}")