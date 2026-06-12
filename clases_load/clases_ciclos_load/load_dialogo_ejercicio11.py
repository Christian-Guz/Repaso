from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio11 import Conteo_impares

class DialogoEjercicio11(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio11.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_conteo_impares)
        
    def mostrar_conteo_impares(self):
        conteo = Conteo_impares()
        conteo.numero = int(self.txt_numero.text())
        self.x = ""
        for i in range(1, conteo.numero + 1):
            if i % 2 != 0:
                if i + 2 > conteo.numero:
                    self.x += f"{i}"
                else:
                    self.x += f"{i}, "
        self.lbl_numeros.setText(self.x)