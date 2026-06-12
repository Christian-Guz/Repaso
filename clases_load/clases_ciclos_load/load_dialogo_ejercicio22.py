from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio22 import Ahorro

class DialogoEjercicio22(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio22.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_ahorro)
        
    def calcular_ahorro(self):
        ahorro = Ahorro()
        ahorro.cantidad = float(self.txt_dinero.text())
        ahorro.tiempo = int(self.txt_tiempo.text())
        ahorro.calcular_ahorro()
        self.lbl_calculo.setText(ahorro.x)