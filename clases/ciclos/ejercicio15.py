class Palabra_reves(object):
  def leer_datos(self):
    self.palabra = input("Palabra = ")

  def imprimir_palabra(self):
    for i in range(len(self.palabra) - 1, -1, -1):
      print(self.palabra[i])