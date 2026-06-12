from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.basicos.ejercicio3 import Funcion

class DialogoActividad3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio3.ui", self)
        self.btn_calcular.clicked.connect(self.calcular)
        
    def calcular(self):
        funcion = Funcion()
        funcion.x = float(self.txt_x.text())
        funcion.μ = float(self.txt_u.text())
        funcion.o = float(self.txt_o.text())
        funcion.calcular_fx()
        self.lbl_resultado.setText(f"fx = {funcion.fx}")