from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio15 import Palabra_reves

class DialogoEjercicio15(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio15.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_palabra)
        
    def mostrar_palabra(self):
        palabra = Palabra_reves()
        palabra.palabra = self.txt_palabra.text()
        x = ""
        for i in range(len(palabra.palabra) - 1, -1, -1):
            x += palabra.palabra[i] + "\n"
        self.lbl_palabra_inv.setText(x)
        