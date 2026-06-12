from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio25 import Palabra_invertida

class DialogoEjercicio25(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio25.ui", self)
        self.btn_invertir.clicked.connect(self.invertir_palabra)
        
    def invertir_palabra(self):
        palabra = Palabra_invertida()
        palabra.palabra = self.txt_frase.text()
        x = ""
        for i in range(len(palabra.palabra)-1, -1, -1):
            x += palabra.palabra[i]
        self.lbl_reversa.setText(x)