from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio4 import Calculo

class DialogoEjercicio4(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio4.ui", self)
        
        self.btn_responder.clicked.connect(self.calcular)
    
    def calcular(self):
        calculo = Calculo()
        calculo.x_centro = float(self.txt_xcentro.text())
        calculo.y_centro = float(self.txt_ycentro.text())
        calculo.radio = float(self.txt_radio.text())
        calculo.x_punto = float(self.txt_xpunto.text())
        calculo.y_punto = float(self.txt_ypunto.text())
        calculo.calcular()
        self.lbl_respuesta.setText(f"{calculo.punto}")