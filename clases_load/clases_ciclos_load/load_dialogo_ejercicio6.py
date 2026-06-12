from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio6 import Sumatoria

class DialogoEjercicio6(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio6.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_serie)
        
    def calcular_serie(self):
        sumatoria = Sumatoria()
        sumatoria.n = int(self.txt_n.text())
        sumatoria.calcular()
        self.lbl_serie.setText(f"Serie = {sumatoria.serie}")