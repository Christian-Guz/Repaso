class Numero(object):
  def leer_datos(self):
    self.numero = int(input("Número = "))

  def imprimir_numero(self):
    for i in range(self.numero, -1, -1):
      if i == 0:
        print(i, end="")
      else:
        print(i, end=", ")
