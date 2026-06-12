from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio5 import Calculo

class DialogoEjercicio5(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio5.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_serie)
        
    def calcular_serie(self):
        calculo = Calculo()
        calculo.n = int(self.txt_n.text())
        calculo.calcular()
        self.lbl_serie.setText(f"Serie = {calculo.serie}")