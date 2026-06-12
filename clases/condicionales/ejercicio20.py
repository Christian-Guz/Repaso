class IMC(object):
  def leer_datos(self):
    self.peso = float(input("Ingrese su peso en kg: "))
    self.estatura = float(input("Ingrese su estatura en metros: "))
    return self.peso, self.estatura

  def calcular_imc(self):
    self.imc = self.peso / (self.estatura ** 2)
    return self.imc

  def comparar(self):
    if self.imc < 18.5:
      self.x = f"IMC = {round(self.imc, 2)} - Bajo peso"
    elif self.imc >= 18.5 and self.imc <= 24.9:
      self.x = f"IMC = {round(self.imc, 2)} - Peso normal"
    elif self.imc >= 25 and self.imc <= 29.9:
      self.x = f"IMC = {round(self.imc, 2)} - Sobrepeso"
    elif self.imc >= 30 and self.imc <= 34.9:
      self.x = f"IMC = {round(self.imc, 2)} - Obesidad grado 1"
    elif self.imc >= 35 and self.imc <= 39.9:
      self.x = f"IMC = {round(self.imc, 2)} - Obesidad grado 2"
    elif self.imc >= 40:
      self.x = f"IMC = {round(self.imc, 2)} - Obesidad grado 3"
    return self.x
  
  def imprimir_resultado(self):
    print(self.x)