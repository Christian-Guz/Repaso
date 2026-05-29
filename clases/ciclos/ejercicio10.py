class Conteo(object):
  def leer_datos(self):
    self.edad = int(input("Edad = "))

  def imprimir_conteo(self):
    for i in range(1, self.edad + 1):
      print(i)