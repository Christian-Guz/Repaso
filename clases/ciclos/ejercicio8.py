class Tablas(object):
  def calcular_tabla(self):
    for i in range(1, 11):
      for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")