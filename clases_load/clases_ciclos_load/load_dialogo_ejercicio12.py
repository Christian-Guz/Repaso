from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio12 import Numero

class DialogoEjercicio12(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio12.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_numeros)
        
    def mostrar_numeros(self):
        numero = Numero()
        numero.numero = int(self.txt_numero.text())
        self.x = ""
        for i in range(numero.numero, - 1, -1):
            if i == 0:
                self.x += str(i) + ""
            else:
                self.x += str(i) + ", "
        self.lbl_numeros.setText(self.x)