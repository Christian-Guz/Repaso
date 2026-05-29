class Venta(object):
  def leer_datos(self):
    self.barras = int(input("Ingrese el numero de barras vendidas que no son del dia: "))
    return self.barras

  def calcular_venta(self):
    self.precio = self.barras * 3.49
    self.descuento = self.precio * 0.6
    self.total = self.precio - self.descuento
    return self.precio, self.descuento, self.total

  def mostrar_venta(self):
    print(f"El precio habitual de una barra de pan es {3.49}€")
    print(f"El descuento que se le hace por no ser fresca es {round(self.descuento,2)}€")
    print(f"El coste final total es {round(self.total,2)}€")