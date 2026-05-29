class Palabra(object):
  def leer_datos(self):
    self.palabra = input("Palabra = ")

  def imprimir_palabra(self):
    for i in range(10):
      print(self.palabra)