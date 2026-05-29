class Numero(object):
  def leer_datos(self):
    self.numero = int(input("Número = "))

  def imprimir_numero(self):
    for i in range(2, self.numero):
      if self.numero % i == 0:
        print("No es un número primo")
        break
    else:
      print("Es un número primo")