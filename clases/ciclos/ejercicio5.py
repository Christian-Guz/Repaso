class Calculo(object):
  def leer_datos(self):
    self.n = int(input("n = "))

  def calcular(self):
    self.serie = 0
    for i in range(1, self.n + 1):
      self.serie += 1 / ((2*i + 1)**2)**0.5

  def imprimir(self):
    print(f"serie = {self.serie}")