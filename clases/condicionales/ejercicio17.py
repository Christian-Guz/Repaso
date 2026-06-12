class Division(object):
    
  def leer_datos(self):
    self.dividendo = int(input("Dividendo = "))
    self.divisor = int(input("Divisor = "))

  def dividir(self):
    if self.divisor == 0:
      self.resultado = "Error: No se puede dividir por cero"
    else:
      self.resultado = f"El resultado de la división es: {self.dividendo / self.divisor}"
  
  def imprimir_resultado(self):
      print(self.resultado)