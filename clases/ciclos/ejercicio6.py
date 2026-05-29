class Sumatoria(object):
  def leer_datos(self):
    self.n = int(input("n = "))

  def calcular(self):
    self.serie = 0
    for k in range(1, self.n + 1):
      self.serie += (1/2.71828)**k
    self.serie /= 3

  def imprimir(self):
    print(f"serie = {self.serie}")