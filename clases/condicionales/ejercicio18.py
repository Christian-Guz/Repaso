class Alumnos(object):
  def leer_datos(self):
    self.nombre = input("Nombre = ")
    self.sexo = input("Sexo = ")

  def comparar_alumnos(self):
    self.grupo = ""
    if self.sexo.lower() == "mujer":
      if self.nombre[0].lower() < "m":
        self.grupo = "Grupo A"
      else:
        self.grupo = "Grupo B"
    if self.sexo.lower() == "hombre":
      if self.nombre[0].lower() > "n":
        self.grupo = "Grupo A"
      else:
        self.grupo = "Grupo B"
  
  def imprimir_grupo(self):
    print(f"El alumno {self.nombre} pertenece al {self.grupo}")