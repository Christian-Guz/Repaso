class Division_div_rest(object):
  def leer_datos(self):
    self.n = int(input("Ingrese el dividendo: "))
    self.m = int(input("Ingrese el divisor: "))
    return self.n, self.m

  def calcular_division(self):
    self.c = self.n // self.m
    self.r = self.n % self.m
    return self.c, self.r