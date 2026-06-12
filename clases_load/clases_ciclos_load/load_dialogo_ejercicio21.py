from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio21 import Division_div_rest

class DialogoEjercicio21(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio21.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_division)
        
    def calcular_division(self):
        division = Division_div_rest()
        division.n = int(self.txt_dividendo.text())
        division.m = int(self.txt_divisor.text())
        division.calcular_division()
        self.lbl_calculo.setText(f"El cociente de la división es {division.c} y el resto es {division.r}")