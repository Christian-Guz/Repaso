from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.ciclos.ejercicio16 import Frase_letra

class DialogoEjercicio16(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio16.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_frase)
        
    def mostrar_frase(self):
        frase = Frase_letra()
        frase.palabra = self.txt_palabra.text()
        frase.letra = self.txt_letra.text()
        frase.bucar_letra()
        self.lbl_muestra.setText(f"La letra '{frase.letra}' aparece {frase.contador} veces en la frase '{frase.palabra}'")