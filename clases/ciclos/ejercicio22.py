class Ahorro(object):
  def leer_datos(self):
    self.cantidad = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
    self.tiempo = int(input("Ingrese el tiempo de años: "))
    return self.cantidad, self.tiempo

  def calcular_ahorro(self):
    for i in range(self.tiempo):
      self.cantidad += self.cantidad + (self.cantidad * 0.04)
      print(f"Cantidad acumulada {round(self.cantidad,2)} despues de {i + 1} años")