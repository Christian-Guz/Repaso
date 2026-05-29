class Alumnos(object):
  def leer_datos(self):
    self.nombre = input("Nombre = ")
    self.sexo = input("Sexo = ")

  def comparar_alumnos(self):
    if self.sexo.lower() == "mujer":
      if self.nombre[0].lower() < "m":
        print("Grupo A")
      else:
        print("Grupo B")
    if self.sexo.lower() == "hombre":
      if self.nombre[0].lower() > "n":
        print("Grupo A")
      else:
        print("Grupo B")