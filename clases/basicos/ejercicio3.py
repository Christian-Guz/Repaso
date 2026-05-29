class Funcion:
  def leer_datos(self):
    self.x = int(input("x = "))
    self.μ = int(input("μ = "))
    self.o = int(input("o = "))

  def calcular_fx(self):
    self.fx = (1/(2*3.1416*self.o)**0.5) * (2.71828)**((1/2)*((self.x - self.μ)/self.o)**2)

  def imprimir_fx(self):
    print(f"fx = {self.fx}")