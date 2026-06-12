class Saludo(object):
  def leer_datos(self):
    self.nombre = input("Nombre = ")

  def saludo(self):
    self.saludo = f"¡Hola {self.nombre}!"
    
  def imprimir_saludo(self):
    print(self.saludo)