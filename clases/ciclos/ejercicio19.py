class Saludo(object):
  def leer_datos(self):
    self.nombre = input("Nombre = ")

  def imprimir_saludo(self):
    print(f"¡Hola {self.nombre}!")