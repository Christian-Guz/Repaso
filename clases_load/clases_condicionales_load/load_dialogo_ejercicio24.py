from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio24 import Entrada

class DialogoEjercicio24(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio24.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_entrada)
        
    def mostrar_entrada(self):
        entrada = Entrada()
        entrada.edad = int(self.txt_edad.text())
        entrada.calcular_entrada()
        self.lbl_precio.setText(f"El precio de la entrada es {entrada.precio}€")
        