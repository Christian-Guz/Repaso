class Entrada(object):
  def leer_datos(self):
    self.edad = int(input("Ingrese la edad del cliente: "))
    return self.edad

  def calcular_entrada(self):
    if self.edad < 4:
      self.precio = 0
    elif self.edad >= 4 and self.edad <= 18:
      self.precio = 5
    elif self.edad > 18:
      self.precio = 10
    return self.precio

  def mostrar_entrada(self):
    print(f"El precio de la entrada es {self.precio}€")