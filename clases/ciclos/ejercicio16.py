class Frase_letra(object):
  def leer_datos(self):
    self.palabra = input("Palabra = ")
    self.letra = input("Letra = ")

  def bucar_letra(self):
    self.contador = 0
    for i in range(len(self.palabra)):
      if self.palabra[i] == self.letra:
        self.contador += 1

  def imprimir_palabra(self):
    print(f"La letra {self.letra} aparece {self.contador} veces en la palabra {self.palabra}")
