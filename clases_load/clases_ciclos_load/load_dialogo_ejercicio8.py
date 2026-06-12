from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class DialogoEjercicio8(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio8.ui", self)
        self.btn_crear.clicked.connect(self.crear_tabla)
        
    def crear_tabla(self):
        for i in range(1,11):
            x = ""
            for j in range(1,11):
                x += f"{i} x {j} = {i * j}\n"
            etiqueta = getattr(self, f"lbl_{i}")
            etiqueta.setText(x)
        