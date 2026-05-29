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
      print(f"IMC = {self.imc} - Bajo peso")
    elif self.imc >= 18.5 and self.imc <= 24.9:
      print(f"IMC = {self.imc} - Peso normal")
    elif self.imc >= 25 and self.imc <= 29.9:
      print(f"IMC = {self.imc} - Sobrepeso")
    elif self.imc >= 30 and self.imc <= 34.9:
      print(f"IMC = {self.imc} - Obesidad grado 1")
    elif self.imc >= 35 and self.imc <= 39.9:
      print(f"IMC = {self.imc} - Obesidad grado 2")
    elif self.imc >= 40:
      print(f"IMC = {self.imc} - Obesidad grado 3")