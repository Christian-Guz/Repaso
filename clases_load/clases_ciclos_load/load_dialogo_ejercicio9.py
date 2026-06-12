from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio9 import Palabra

class DialogoEjercicio9(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio9.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_palabra)
        
    def mostrar_palabra(self):
        palabra = Palabra()
        palabra.palabra = self.txt_palabra.text()
        self.x = ""
        for i in range(10):
            self.x += palabra.palabra + "\n"
        self.lbl_palabras.setText(self.x)