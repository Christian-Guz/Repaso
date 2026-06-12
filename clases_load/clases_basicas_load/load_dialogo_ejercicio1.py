from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.basicos.ejercicio1 import Recta

class DialogoEjercicio1(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio1.ui", self)
        self.btn_calcular.clicked.connect(self.calcular)
    
    def calcular(self):
        recta = Recta(0, 0, 0, 0)
        recta.x1 = float(self.txt_x1.text())
        recta.y1 = float(self.txt_y1.text())
        recta.x2 = float(self.txt_x2.text())
        recta.y2 = float(self.txt_y2.text())
        recta.calcular_pendiente()
        self.lbl_resultado.setText(f"m: {recta.m}")