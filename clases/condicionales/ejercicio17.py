class Division(object):
    
  def leer_datos(self):
    self.dividendo = int(input("Dividendo = "))
    self.divisor = int(input("Divisor = "))

  def dividir(self):
    if self.divisor == 0:
      print("Error: No se puede dividir por cero")
    else:
      self.cociente = self.dividendo / self.divisor
      print(f"El resultado de la división es {self.cociente}")