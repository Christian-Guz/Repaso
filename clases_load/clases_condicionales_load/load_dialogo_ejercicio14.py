from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio14 import Numero

class DialogoEjercicio14(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio14.ui", self)
        self.btn_mostrar.clicked.connect(self.calcular_numero)
        
    def calcular_numero(self):
        numero = Numero()
        numero.numero = int(self.txt_numero.text())
        numero.imprimir_numero()
        self.lbl_muestra.setText(numero.x)