from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio19 import Saludo

class DialogoEjercicio19(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio19.ui", self)
        self.btn_saludar.clicked.connect(self.saludar)
    
    def saludar(self):
        saludo = Saludo()
        saludo.nombre = self.txt_nombre.text()
        saludo.saludo()
        self.lbl_saludo.setText(saludo.saludo)