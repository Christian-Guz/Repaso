class Conteo_impares(object):
  def leer_datos(self):
    self.numero = int(input("Número = "))

  def imprimir_conteo(self):
    for i in range(1, self.numero + 1):
      if i % 2 != 0:
        if i + 2 > self.numero:
          print(i, end="")
        else:
          print(i, end=", ")
