from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio13 import Inversion

class DialogoEjercicio13(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio13.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_inversion)
        
    def calcular_inversion(self):
        inversion = Inversion()
        inversion.cantidad = float(self.txt_inversion.text())
        inversion.interes = float(self.txt_interes.text())
        inversion.años = int(self.txt_num.text())
        self.x = ""
        for i in range(1, inversion.años + 1):
            inversion.cantidad *= (1 + inversion.interes / 100)
            self.x += f"Año {i}: {inversion.cantidad}\n"
        self.lbl_calculo.setText(self.x)