from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio20 import IMC

class DialogoEjercicio20(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio20.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_imc)
        
    def calcular_imc(self):
        imc = IMC()
        imc.peso = float(self.txt_kg.text())
        imc.estatura = float(self.txt_metros.text())
        imc.calcular_imc()
        imc.comparar()
        self.lbl_calculo.setText(imc.x)