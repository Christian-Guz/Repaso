from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio23 import Venta

class DialogoEjercicio23(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio23.ui", self)
        self.btn_calcular.clicked.connect(self.calcular_venta)
        
    def calcular_venta(self):
        venta = Venta()
        venta.barras = int(self.txt_pan.text())
        venta.calcular_venta()
        self.lbl_original.setText(f"El precio habitual de una barra de pan es 3.49€")
        self.lbl_descuento.setText(f"El descuento que se le hace por no ser fresca es {round(venta.descuento,2)}€")
        self.lbl_final.setText(f"El coste final total es {round(venta.total,2)}€")