from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio10 import Conteo

class DialogoEjercicio10(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio10.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_conteo)
        
    def mostrar_conteo(self):
        conteo = Conteo()
        conteo.edad = int(self.txt_edad.text())
        self.x = ""
        for i in range(1, conteo.edad + 1):
            if i < 10:
                self.x += f"Has cumplido {i} año\n"
            if i >= 10:
                self.x += f"Has cumplido {i} años\n" 
        self.lbl_edades.setText(self.x) 