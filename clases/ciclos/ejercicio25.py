class Palabra_invertida(object):
  def leer_datos(self):
    self.palabra = input("Ingrese una frase: ")
    return self.palabra

  def invertir_palabra(self):
    for i in range(len(self.palabra) - 1, -1, -1):
      print(self.palabra[i], end="")