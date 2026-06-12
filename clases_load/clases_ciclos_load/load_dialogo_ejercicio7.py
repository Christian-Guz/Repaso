from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio7 import Tabla

class DialogoEjercicio7(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio7.ui", self)
        self.btn_crear.clicked.connect(self.crear_tabla)
        
    def crear_tabla(self):
        tabla = Tabla()
        tabla.n = int(self.txt_numero.text())
        self.x = ""
        for i in range(1,11):
            self.x += f"{tabla.n} x {i} = {tabla.n * i}\n"
        self.lbl_tabla.setText(self.x)