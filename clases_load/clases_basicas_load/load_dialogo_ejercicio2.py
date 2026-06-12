from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.basicos.ejercicio2 import Distancia

class DialogoEjercicio2(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio2.ui", self)
        self.btn_calcular.clicked.connect(self.calcular)
        
    def calcular(self):
        distancia = Distancia()
        distancia.x1 = float(self.txt_x1.text())
        distancia.x2 = float(self.txt_x2.text())
        distancia.y1 = float(self.txt_y1.text())
        distancia.y2 = float(self.txt_y2.text())
        distancia.calcular_distancia()
        self.lbl_distancia.setText(f"d = {distancia.d}")
