from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio17 import Division

class DialogoEjercicio17(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio17.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_division)
        
    def calcular_division(self):
        division = Division()
        division.dividendo = int(self.txt_dividendo.text())
        division.divisor = int(self.txt_divisor.text())
        division.dividir()
        self.lbl_resultado.setText(division.resultado)